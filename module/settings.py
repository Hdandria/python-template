from typing import Dict

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class AppSettings(BaseSettings):
    """Application-specific settings."""

    app_name: str = Field(default="Python Template", description="Application name")
    dev_mode: bool = Field(default=False, description="Enable dev mode for development-specific features")


class LogSettings(BaseSettings):
    """Logging configuration settings."""

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


class Settings(BaseSettings):
    """
    Main settings class that composes all other settings.
    This class automatically loads configuration from environment variables and .env files.
    """

    app: AppSettings = AppSettings()
    log: LogSettings = LogSettings()

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        env_nested_delimiter="__",
    )


# Create global settings instance
settings = Settings()
