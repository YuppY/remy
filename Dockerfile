FROM python:3
ENV PYTHONUNBUFFERED 1
ENV DJANGO_LOG_LEVEL DEBUG

RUN apt-get update && apt-get -y install wait-for-it

COPY app/requirements.txt /app/
WORKDIR /app
RUN pip install -r requirements.txt

COPY app/ /app/
