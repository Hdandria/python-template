# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app

# Set environment variables for Python for best practices
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install uv using pip
RUN pip install uv

# Copy dependency definition files first to leverage Docker's layer caching
COPY pyproject.toml uv.lock ./

# Install dependencies into the system's Python environment
# Using --locked ensures reproducible builds from the lock file
RUN uv sync --locked

# Copy the rest of the application's source code
COPY module/ ./module/
COPY scripts/ ./scripts/

# Set the default command to run the application using uv
CMD ["uv", "run", "python", "-m", "module"]
