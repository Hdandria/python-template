---
description: Global project instructions, code standards, and architecture.
globs:
alwaysApply: true
---

# Project Instructions

## Code Standards

- Use Python 3.12+ with `uv` for dependency management.
- Always use type hints for functions.
- Use `pydantic-settings` for configuration (`src/module/settings.py`).
- Use `structlog` for logging. `print` is forbidden.
- Format code with `ruff`.
- Always type your functions. Generic `dict` types / `Any` are forbidden.
- If making API calls, always define Pydantic objects to parse the responses.
- Non-trivial function must have an explicit docstring that immediately defines the function's behavior.
- Always favor async functions for API calls. Handle all concurrency with `asyncio`.
- For any file or path manipulation, exclusively use `pathlib.Path`. Usage of `os.path` or raw strings for paths is forbidden.

## Architecture

- Source code in `src/`.
- Configuration must be loaded from `src/module/settings.py` via `from module.settings import settings`.
- Logging must be initialized at the entry point via `setup_logging()`.

## Packaging

- Never install anything yourself. If packages are missing, ask the user to install them.

## Scripts

When running Python commands, always prefix them with `uv run`, otherwise you will not run them with the correct Python environment.

## Behavior

- If your changes require deep code modifications and changing multiple functions, ask the user for validation. Explain your plan and what improvements it brings.
- If your changes are basic / direct applications of what the user asked, act directly. No unnecessary validation.

## Unit Tests

- After every significant feature development, create quick tests in the `/tests` folder. You can `import from module...` (assuming the module is installed via `pip -e`).
- Your unit tests must be fast and simple. No real API calls. If they require creating complex objects, ask the user for their opinion. If you can implement tests quickly, do them immediately.
- Your tests will be executed with `pytest`. Always prefix them with `test` (e.g., `test_sometest`).
