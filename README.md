# Python Project Template

A simple Python project template with structured logging, configuration management, and development best practices.

## Quick Start

1. **Clone and install:**

   ```bash
   git clone <repository-url>
   cd python-template
   uv venv
   uv sync
   ```

2. **Run the project:**
   ```bash
   uv run python -m module # uv prefix only if you didn't activate your venv yet.
   ```

## Prerequisites

- Python 3.12+
- [uv](https://docs.astral.sh/uv/) package manager

## Project Structure

```
python-template/
├── module/                 # Main package
│   ├── __init__.py
│   ├── __main__.py        # Entry point
│   ├── settings.py        # Configuration management
│   └── logger_config.py   # Logging setup
├── scripts/               # Utility scripts
├── pyproject.toml         # Project configuration
└── README.md             # This file
```

## Configuration

Create a `.env` file from `.env.example` and customize your settings:

```bash
cp .env.example .env
```

The template uses `pydantic-settings` for type-safe configuration management with automatic environment variable loading.

## Logging

Uses `structlog` for structured logging with automatic log rotation:

```python
import structlog

logger = structlog.get_logger()
logger.info("Application started", user_id=123)
logger.error("Error occurred", error_code="E001")
```

Logs are written to both console (pretty format) and files (JSON format) with automatic rotation.

## Scripts

Utility scripts in the `scripts/` directory:

- `check_env.py` - Verify .env configuration

```bash
uv run python scripts/check_env.py
```

## Development

### Type Hints

All functions must have type hints:

```python
def process_data(data: List[Dict[str, Any]], config: Optional[Dict[str, str]] = None) -> bool:
    """Process the given data with optional configuration."""
    return True
```

### Guidelines

- Use `module/` package for application code
- Add dependencies with `uv add <package>`
- Keep configuration environment-configurable
- Never commit `.env` files

## Getting Started

1. Clone this template
2. Update `pyproject.toml` with your project details
3. Create `.env` from `.env.example` and configure
4. Start developing!
