FROM python:3.10-slim

RUN mkdir /hotels

WORKDIR /hotels

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

# CMD ["gunicorn", "app.main:app", "--workers", "2", "--worker-class", "uvicorn.workers.UvicornWorker", "--bind=0.0.0.0:8000"]