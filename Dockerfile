# Container image that runs your code
FROM python:3.8.3-slim

ENV PYTHONUNBUFFERED 1

RUN apt-get update
RUN apt-get install -y default-libmysqlclient-dev python-dev build-essential

RUN mkdir /app

WORKDIR /app

COPY requirements.txt /etc/requirements.txt

RUN pip install -r /etc/requirements.txt

COPY . /app/

EXPOSE 80
CMD gunicorn core.wsgi -b 0.0.0.0:8000 --log-file -