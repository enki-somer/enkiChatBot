FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY test_widget.html .
COPY serve_test_widget.py .

ENV FLASK_APP=serve_test_widget.py
ENV FLASK_ENV=production
ENV PORT=3000
# The RASA_URL will be provided by Railway environment variables
# or can be set directly here if needed

EXPOSE 3000

# Start the server with gunicorn for better production performance
CMD gunicorn serve_test_widget:app --bind 0.0.0.0:$PORT --timeout 120 