from dotenv import load_dotenv

load_dotenv()

from .logger_config import setup_logging  # noqa: E402

setup_logging()
