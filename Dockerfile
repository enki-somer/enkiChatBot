FROM python:3.8-slim

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

# Command to run when the container starts
CMD rasa run --enable-api --cors "*" --credentials credentials_railway.yml --port $PORT 