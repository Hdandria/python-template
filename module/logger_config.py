import logging
import sys
from datetime import datetime
from pathlib import Path

import structlog

from module.settings import settings


def setup_logging():
    """
    Centralized logging setup for the backend. Configures log level, format, and logger filtering.
    Sets up dual logging: pretty, human-readable logs to console, and JSON logs to file (app.log),
    using structlog renderers. Should be called at the entry point of any backend script or server.
    """
    root_logger = logging.getLogger()
    root_logger.setLevel(settings.log_level)
    for handler in root_logger.handlers[:]:
        root_logger.removeHandler(handler)

    # Console handler (pretty)
    # Reconfigure stdout to handle UTF-8, fixing Unicode errors in console logs.
    # This is more compatible than passing the 'encoding' argument to StreamHandler.
    sys.stdout.reconfigure(encoding="utf-8")  # type: ignore
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(settings.log_level)
    # File handler (JSON)
    log_date = datetime.now().strftime("%Y-%m-%d")
    log_dir = Path("logs") / log_date
    log_dir.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    log_file = log_dir / f"app_{timestamp}.log"
    file_handler = logging.FileHandler(str(log_file), mode="w", encoding="utf-8")
    file_handler.setLevel(settings.log_level)

    # Use structlog's ProcessorFormatter for both handlers
    pre_chain = [
        structlog.processors.TimeStamper(fmt="%m/%d %H:%M:%S"),
        structlog.stdlib.add_log_level,
        structlog.stdlib.add_logger_name,
        structlog.processors.format_exc_info,
    ]
    console_handler.setFormatter(
        structlog.stdlib.ProcessorFormatter(
            processor=structlog.dev.ConsoleRenderer(
                colors=True, exception_formatter=structlog.dev.plain_traceback
            ),
            foreign_pre_chain=pre_chain,
        )
    )
    file_handler.setFormatter(
        structlog.stdlib.ProcessorFormatter(
            processor=structlog.dev.ConsoleRenderer(
                colors=False, exception_formatter=structlog.dev.plain_traceback
            ),
            foreign_pre_chain=pre_chain,
        )
    )
    root_logger.addHandler(console_handler)
    root_logger.addHandler(file_handler)

    # Apply log level overrides from settings
    for logger_name, level in settings.logger_level_overrides.items():
        log_level = getattr(logging, level.upper(), None)
        if isinstance(log_level, int):
            logging.getLogger(logger_name).setLevel(log_level)

    # --- structlog configuration ---
    structlog.configure(
        processors=[
            structlog.contextvars.merge_contextvars,
            structlog.stdlib.filter_by_level,
            structlog.stdlib.add_logger_name,
            structlog.stdlib.add_log_level,
            structlog.processors.TimeStamper(fmt="%m/%d %H:%M:%S"),
            structlog.stdlib.ProcessorFormatter.wrap_for_formatter,
        ],
        wrapper_class=structlog.stdlib.BoundLogger,
        context_class=dict,
        logger_factory=structlog.stdlib.LoggerFactory(),
        cache_logger_on_first_use=True,
    )
