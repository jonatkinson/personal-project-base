FROM python:3.8.3-slim

ENV PYTHONUNBUFFERED 1

RUN useradd -m user
USER user
WORKDIR /home/user
ENV PATH="/home/user/.local/bin:${PATH}"

COPY . /home/user

RUN pip --disable-pip-version-check install --upgrade pip
RUN pip install -r ./requirements.txt

EXPOSE 80
CMD gunicorn core.wsgi -b 0.0.0.0:8000 --log-file -