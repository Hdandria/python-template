from pathlib import Path
from typing import Dict

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

# Determine project root based on this file's location: src/core/settings.py -> ../../.. -> project root
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
ENV_FILE = PROJECT_ROOT / ".env"


class AppSettings(BaseSettings):
    """Application-specific settings."""

    model_config = SettingsConfigDict(env_prefix="APP_", env_file=ENV_FILE, extra="ignore")

    name: str = Field(default="Python Template", description="Application name")
    dev_mode: bool = Field(default=False, description="Enable dev mode for development-specific features")


class LogSettings(BaseSettings):
    """Logging configuration settings."""

    model_config = SettingsConfigDict(env_prefix="LOG_", env_file=ENV_FILE, extra="ignore")

    level: str = Field(
        default="INFO",
        description="Logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)",
    )
    dir: str = Field(default="logs", description="Directory for log files")
    file: str = Field(default="app.log", description="Main log file name")
    max_bytes: int = Field(default=10485760, description="Maximum size of log file before rotation (10MB)")
    backup_count: int = Field(default=5, description="Number of backup log files to keep")
    level_overrides: Dict[str, str] = Field(
        default_factory=dict,
        description="Override log levels for specific loggers (e.g., {'module.submodule': 'DEBUG'})",
    )


class Settings(BaseSettings):
    """
    Main settings class that composes all other settings.
    """

    app: AppSettings = Field(default_factory=AppSettings)
    log: LogSettings = Field(default_factory=LogSettings)


# Create global settings instance
settings = Settings()
