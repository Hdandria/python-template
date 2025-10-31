import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path
import sys
from typing import Union

import structlog
from structlog.types import Processor

from module.settings import settings


def setup_logging() -> None:
    """
    Centralized logging setup for the backend. Configures log level, format, and logger filtering.
    Sets up dual logging: pretty, human-readable logs to console (if DEV=True), and JSON logs to file (app.log),
    using structlog renderers. Should be called at the entry point of any backend script or server.
    """
    # Reconfigure stdout to handle UTF-8, fixing Unicode errors in console logs.
    # This is more compatible than passing the 'encoding' argument to StreamHandler.
    sys.stdout.reconfigure(encoding="utf-8")  # type: ignore

    # Define shared processors for structlog
    shared_processors: list[Processor] = [
        structlog.contextvars.merge_contextvars,
        structlog.stdlib.add_logger_name,
        structlog.stdlib.add_log_level,
        structlog.processors.format_exc_info,
        structlog.processors.TimeStamper(fmt="%H:%M:%S"),
    ]

    # Determine the renderer for console output based on dev mode
    console_renderer: Union[structlog.dev.ConsoleRenderer, structlog.processors.JSONRenderer]
    if settings.app.dev_mode:
        console_renderer = structlog.dev.ConsoleRenderer(colors=True, exception_formatter=structlog.dev.plain_traceback)
    else:
        # In production (dev_mode=False), use JSONRenderer for structured logging,
        # which is compatible with cloud logging platforms like GCP Cloud Logging.
        console_renderer = structlog.processors.JSONRenderer()

    # Configure structlog
    structlog.configure(
        processors=[
            *shared_processors,
            structlog.stdlib.ProcessorFormatter.wrap_for_formatter,
        ],
        logger_factory=structlog.stdlib.LoggerFactory(),
        wrapper_class=structlog.stdlib.BoundLogger,
        cache_logger_on_first_use=True,
    )

    # --- Standard library logging configuration ---

    # Console handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(settings.log.log_level)
    console_handler.setFormatter(
        structlog.stdlib.ProcessorFormatter(
            processor=console_renderer,
            foreign_pre_chain=shared_processors,
        )
    )

    # Handlers configuration
    handlers: list[logging.Handler] = [console_handler]
    if not settings.app.dev_mode:
        # File handler (JSON) - only enabled in production mode
        log_dir = Path(settings.log.log_dir)
        log_dir.mkdir(parents=True, exist_ok=True)
        log_file = log_dir / settings.log.log_file

        file_handler = RotatingFileHandler(
            str(log_file),
            mode="a",
            encoding="utf-8",
            maxBytes=settings.log.log_max_bytes,
            backupCount=settings.log.log_backup_count,
        )
        file_handler.setLevel(settings.log.log_level)
        file_handler.setFormatter(
            structlog.stdlib.ProcessorFormatter(
                processor=structlog.processors.JSONRenderer(),
                foreign_pre_chain=shared_processors,
            )
        )
        handlers.append(file_handler)

    # Configure root logger
    root_logger = logging.getLogger()
    root_logger.setLevel(settings.log.log_level)
    root_logger.handlers = handlers  # Replace existing handlers

    # Apply log level overrides from settings
    for logger_name, level in settings.log.logger_level_overrides.items():
        log_level = getattr(logging, level.upper(), None)
        if isinstance(log_level, int):
            logging.getLogger(logger_name).setLevel(log_level)
