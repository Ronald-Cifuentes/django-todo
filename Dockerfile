FROM python:3.11-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install system deps for psycopg2
RUN apt-get update && apt-get install -y --no-install-recommends \
    libpq5 \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Create non-root user
RUN adduser --disabled-password --gecos '' appuser && chown -R appuser /app
USER appuser

# Render.com sets PORT at runtime
ENV PORT=4001
EXPOSE 4001

# Gunicorn: bind to 0.0.0.0 and use PORT from env
CMD ["sh", "-c", "python manage.py migrate --noinput && gunicorn todoapp.wsgi:application --bind 0.0.0.0:${PORT} --workers 1 --threads 2 --access-logfile -"]
