# Python Project Template

A simple Python project template with structured logging, configuration management, and development best practices.

## Features

- **Dependency Management**: Uses [`uv`](https://docs.astral.sh/uv/) for fast and reliable dependency management.
- **Configuration**: Type-safe configuration management with [`pydantic-settings`](https://docs.pydantic.dev/latest/concepts/pydantic_settings/).
- **Logging**: Structured logging with [`structlog`](https://www.structlog.org/en/stable/).
- **Code Quality**: Automated code formatting, linting, and import sorting with [`Ruff`](https://docs.astral.sh/ruff/).
- **Testing**: Test suite setup with [`pytest`](https://docs.pytest.org/en/latest/).
- **Pre-commit Hooks**: Ensures code quality before every commit.
- **CI/CD**: Continuous Integration with GitHub Actions to automate testing and quality checks.
- **Containerization**: `Dockerfile` included for easy containerization.

## Quick Start

1.  **Clone the repository and create a virtual environment:**

    ```bash
    git clone <repository-url>
    cd python-template
    uv venv
    source .venv/bin/activate  # On Windows, use `.venv\Scripts\activate`
    ```

2.  **Install dependencies and the package in editable mode:**
    To ensure that scripts can correctly import the project module, you must install the package in editable (`-e`) mode.

    ```bash
    uv sync --dev
    uv pip install -e .
    ```

3.  **Set up pre-commit hooks (optional but recommended):**

    ```bash
    pre-commit install
    ```

4.  **Run the project:**
    ```bash
    python -m module
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
├── tests/                 # Test suite
├── .github/               # GitHub Actions workflows
├── .pre-commit-config.yaml # Pre-commit hook configuration
├── Dockerfile             # Containerization file
├── LICENSE                # Project License
├── pyproject.toml         # Project configuration
└── README.md              # This file
```

## Configuration

Create a `.env` file from `.env.example` and customize your settings:

```bash
cp .env.example .env
```

The template uses `pydantic-settings` for type-safe configuration management with automatic environment variable loading.

## Logging

Uses `structlog` for structured logging. Logs are written to both the console (in a human-readable format) and to files (in JSON format) with automatic rotation.

```python
import structlog

logger = structlog.get_logger()
logger.info("Application started", user_id=123)
logger.error("Error occurred", error_code="E001")
```

## Code Quality

This project uses [Ruff](https://docs.astral.sh/ruff/) to handle linting, formatting, and import sorting. The configuration is defined in `pyproject.toml`.

To check and format your code, you can run:

```bash
# Check for linting errors
uv run ruff check .

# Format your code
uv run ruff format .
```

Pre-commit hooks are also configured to run these checks automatically before each commit.

## Testing

Tests are located in the `tests/` directory and are run with `pytest`.

```bash
uv run pytest
```

The test suite is also automatically run by the CI pipeline on every push and pull request.

## Scripts

Utility scripts in the `scripts/` directory:

- `check_env.py` - Verify .env configuration

To run the scripts, make sure you have installed the package in editable mode as described in the Development section.

```bash
python scripts/check_env.py
```

## Development

### Type Hints

All functions must have type hints:

```python
def process_data(data: list[dict[str, any]], config: dict[str, str] | None = None) -> bool:
    """Process the given data with optional configuration."""
    return True
```

### Guidelines

- Use `module/` package for application code
- Add dependencies with `uv add <package>`
- Keep configuration environment-configurable
- Never commit `.env` files

### Editable Install for Development

When developing, you should install the project package in "editable" or "develop" mode. This allows you to run scripts from the project root and have them correctly import your application code from the `module/` directory.

It also ensures that any changes you make to the Python code are immediately available without needing to reinstall the package.

```bash
uv pip install -e .
```

This command should be run after you have created your virtual environment and installed the dependencies with `uv sync`.

## Containerization

A `Dockerfile` is provided to build a Docker image for the application.

```bash
# Build the image
docker build -t python-template .

# Run the container
docker run python-template
```

## Getting Started

1.  Clone this template
2.  Update `pyproject.toml` with your project details
3.  Create `.env` from `.env.example` and configure
4.  Install pre-commit hooks: `uv run pre-commit install`
5.  Start developing!
