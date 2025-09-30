# Python Project Template

This repository serves as a template for all Python projects within the enterprise. It provides a standardized structure, configuration, and best practices for Python development.

## Table of Contents

- [Installation](#installation)
- [Project Structure](#project-structure)
- [Environment Configuration](#environment-configuration)
- [Logging with Structlog](#logging-with-structlog)
- [Settings Management](#settings-management)
- [Development Guidelines](#development-guidelines)

## Installation

### Prerequisites

- Python 3.12 or higher
- [uv](https://docs.astral.sh/uv/) package manager

1. **Clone the repository:**

   ```bash
   git clone <repository-url>
   cd python-template
   ```

2. **Install dependencies:**

   ```bash
   uv sync
   ```

3. **Activate the virtual environment:**

   ```bash
   # On Windows
   .venv\Scripts\activate

   # On macOS/Linux
   source .venv/bin/activate
   ```

4. **Run the project:**
   ```bash
   uv run python -m module
   ```

## Project Structure

```
python-template/
├── module/                 # Main package
│   ├── __init__.py
│   ├── __main__.py        # Entry point
│   ├── settings.py        # Configuration management
│   └── logger_config.py   # Logging setup
├── pyproject.toml         # Project configuration
├── .env.example          # Environment variables template
├── .env                  # Environment variables (create from .env.example)
└── README.md             # This file
```

## Environment Configuration

### Setting up .env

1. **Copy the example file:**

   ```bash
   cp .env.example .env
   ```

2. **Edit the .env file** with your specific configuration values.

3. **Never commit .env files** - they are already in .gitignore.

### Environment Variables

The `.env.example` file contains all the necessary environment variables for the project. Each variable includes:

- A description of its purpose
- Default values where applicable
- Required vs optional status

## Logging with Structlog

This template uses `structlog` for structured logging instead of `print()` statements. Structlog provides structured data, multiple output formats, context variables, and better performance.

### Quick Start

```python
import structlog

logger = structlog.get_logger()
logger.info("Application started", user_id=123)
logger.error("Error occurred", error_code="E001")
```

### Configuration

Logging is configured in `module/logger_config.py` with console (pretty) and file (JSON) outputs.

**For detailed documentation, see:** [Structlog Documentation](https://www.structlog.org/en/stable/)

## Settings Management

This template uses `pydantic-settings` for configuration management with type safety, environment variable loading, and validation.

See `module/settings.py` for configuration examples.

**For detailed documentation, see:** [Pydantic Settings Documentation](https://docs.pydantic.dev/latest/concepts/pydantic_settings/)

## Scripts

The `scripts/` directory contains utility scripts for common tasks. All scripts automatically add the project root to the Python path, allowing them to import from the `module/` package.

### Available Scripts

- **`check_env.py`** - Verify that .env configuration is set correctly

### Running Scripts

```bash
# Run from project root
python scripts/check_env.py

# Or using uv
uv run python scripts/check_env.py
```

## Development Guidelines

### Type Hints

All functions must be defined with type hints:

```python
from typing import List, Optional, Dict, Any
from pydantic import BaseModel

def process_data(data: List[Dict[str, Any]], config: Optional[Dict[str, str]] = None) -> bool:
    """Process the given data with optional configuration."""
    # Implementation here
    return True

class UserModel(BaseModel):
    id: int
    name: str
    email: str
    is_active: bool = True
```

### Code Organization

- Use the `module/` package for your main application code
- Keep configuration in `settings.py`
- Use `logger_config.py` for logging setup
- Add new modules as needed within the `module/` package

### Dependencies

- Add new dependencies to `pyproject.toml`
- Use `uv add <package>` for adding dependencies
- Keep dependencies minimal and well-documented

### Environment Variables

- All configuration should be environment-configurable
- Use `.env.example` to document required variables
- Never commit actual `.env` files
- Use descriptive variable names with clear documentation

## Getting Started

1. Clone this template
2. Update `pyproject.toml` with your project details
3. Copy `.env.example` to `.env` and configure
4. Update `module/settings.py` with your specific configuration
5. Start developing your application!

## Support

For questions or issues with this template, please contact the development team or create an issue in the repository.
