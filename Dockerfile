FROM python:3.12-slim
WORKDIR /app
COPY eda.ipynb .
ENTRYPOINT ["python3", "eda.ipynb"]