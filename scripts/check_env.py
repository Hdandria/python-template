#!/usr/bin/env python3
"""
Script to check if .env configuration is set correctly.
This script reads from the module settings and displays the current configuration.
"""

from pathlib import Path
import sys

import structlog

from module.logger_config import setup_logging
from module.settings import settings

project_root = Path(__file__).parent.parent


def check_env() -> bool:
    """Check and display the current environment configuration."""
    # Setup logging
    setup_logging()
    logger = structlog.get_logger("env_check")

    logger.info("Starting .env configuration check")

    try:
        # Display current settings
        logger.info(
            "Current configuration",
            app_name=settings.app.app_name,
            dev_mode=settings.app.dev_mode,
            log_level=settings.log.log_level,
            log_dir=settings.log.log_dir,
            log_file=settings.log.log_file,
        )

        # Check if .env file exists
        env_file = project_root / ".env"
        if env_file.exists():
            logger.info("Environment file found", env_file=str(env_file))
        else:
            logger.error(
                "Environment file not found",
                env_file=str(env_file),
                message=".env file is required!",
                instructions="Create one from .env.example: cp .env.example .env",
            )
            return False

        # Check log directory
        log_dir = Path(settings.log.log_dir)
        if log_dir.exists():
            logger.info("Log directory exists", log_dir=str(log_dir))
        else:
            logger.warning(
                "Log directory not found",
                log_dir=str(log_dir),
                message="It will be created when first log is written",
            )

        logger.info("Configuration check completed successfully")
        return True

    except Exception as e:
        logger.error("Configuration check failed", error=str(e))
        return False


if __name__ == "__main__":
    success = check_env()
    if not success:
        # Setup logging for error message
        setup_logging()
        logger = structlog.get_logger("env_check")
        logger.error("Configuration check failed - exiting")
        sys.exit(1)
