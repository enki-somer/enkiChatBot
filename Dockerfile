FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY test_widget.html .
COPY serve_test_widget.py .

ENV FLASK_APP=serve_test_widget.py
ENV FLASK_ENV=production

CMD ["python", "serve_test_widget.py"] 