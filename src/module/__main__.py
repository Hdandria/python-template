import structlog

from module.logger_config import setup_logging
from module.settings import settings

if __name__ == "__main__":
    setup_logging()
    logger = structlog.get_logger()

    logger.info("Module started")
    logger.info(
        "Module configuration loaded",
        app_name=settings.app.name,
        dev_mode=settings.app.dev_mode,
    )
    logger.info("Module stopped")
