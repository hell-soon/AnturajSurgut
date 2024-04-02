FROM python:3.12-slim
ENV PYTHONUNBUFFERED=1
WORKDIR /backend
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . .