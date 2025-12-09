# Lightweight Python base
FROM python:3.12-slim

# Avoid interactive prompts
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Workdir inside container
WORKDIR /app

# System deps (for compiling, bash, etc.)
RUN apt-get update && apt-get install -y --no-install-recommends \
    bash \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy project code
COPY . /app/

# Expose port
EXPOSE 8000

# Collect static (optional if you use it)
# RUN python manage.py collectstatic --noinput

# Run via daphne (ASGI server for Channels)
CMD ["daphne", "-b", "0.0.0.0", "-p", "8000", "cmdpanel.asgi:application"]
