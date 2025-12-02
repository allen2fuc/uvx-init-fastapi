FROM python:3.13-slim

# Set working directory
WORKDIR /app

# Install system dependencies for OpenCV and curl (for uv installation)
RUN apt-get update && apt-get install -y \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender-dev \
    libgomp1 \
    libgl1 \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Install uv and ensure it's in PATH
COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv
RUN chmod +x /usr/local/bin/uv && \
    /usr/local/bin/uv --version

# Copy dependency files
COPY pyproject.toml ./

# Install Python dependencies using uv sync (creates .venv)
RUN /usr/local/bin/uv sync --no-dev

# Copy application code
COPY app ./app

# Add .venv/bin to PATH for easier access
ENV PATH="/app/.venv/bin:${PATH}"

# Expose port
EXPOSE 8000

# Run the application using uvicorn from the virtual environment (more reliable)
CMD ["uv", "run", "fastapi", "run", "app.app:app", "--host", "0.0.0.0", "--port", "8000"]
