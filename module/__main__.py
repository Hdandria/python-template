import structlog

if __name__ == "__main__":
    logger = structlog.get_logger()
    logger.info("Application started")
    logger.info("Application stopped")
