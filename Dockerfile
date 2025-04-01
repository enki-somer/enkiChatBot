FROM python:3.8-slim AS base

WORKDIR /app

# Install system dependencies
RUN apt-get update -qq && \
    apt-get install -y --no-install-recommends \
    build-essential \
    wget \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip setuptools wheel && \
    pip install --no-cache-dir -r requirements.txt

# Copy the rest of the code
COPY . .

# Train the model
RUN python -m rasa train

# Main Rasa service
FROM base AS rasa
EXPOSE 5005
CMD rasa run --enable-api --cors "*" --credentials credentials_railway.yml --port $PORT

# Actions service
FROM base AS actions
EXPOSE 5055
CMD rasa run actions --port 5055

# Test widget service
FROM base AS widget
EXPOSE 8080
CMD python serve_test_widget.py 