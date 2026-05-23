FROM python:3.10-alpine AS Builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

FROM python:3.10-alpine
WORKDIR /app
COPY --from=builder /usr/local/lib/python3.10/site-packages /usr/local/lib/python3.10/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin
COPY app/ .
EXPOSE 8000
CMD ["gunicorn", "main:app", "--worker-class", "uvicorn.workers.UvicornWorker", "--access-logfile", "-", "--error-logfile", "-", "--capture-output", "--log-level", "info", "--bind", "0.0.0.0:8000"]
