from typing import Dict

from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """
    Application settings using pydantic-settings for type-safe configuration management.

    This class automatically loads configuration from:
    1. Environment variables
    2. .env file
    3. Default values (as defined in Field defaults)
    """

    # Application Configuration
    app_name: str = Field(default="Python Template", description="Application name")
    debug: bool = Field(default=False, description="Enable debug mode for development")
    environment: str = Field(
        default="development",
        description="Environment (development, staging, production)",
    )
    log_level: str = Field(
        default="INFO",
        description="Logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)",
    )
    log_dir: str = Field(default="logs", description="Directory for log files")
    log_file: str = Field(default="app.log", description="Main log file name")
    log_max_bytes: int = Field(default=10485760, description="Maximum size of log file before rotation (10MB)")
    log_backup_count: int = Field(default=5, description="Number of backup log files to keep")
    logger_level_overrides: Dict[str, str] = Field(
        default_factory=dict,
        description="Override log levels for specific loggers (e.g., {'module.submodule': 'DEBUG'})",
    )

    class Config:
        """Pydantic configuration."""

        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = False


# Create global settings instance
settings = Settings()
