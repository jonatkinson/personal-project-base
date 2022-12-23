FROM python:3.11.1-slim

# Python configuration.
ENV PYTHONFAULTHANDLER=1 \
    PYTHONUNBUFFERED=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100

# Poetry configuration.
ENV POETRY_VERSION=1.3.1 \
    POETRY_HOME=/home/user/poetry \
    POETRY_VENV=/home/user/venv \
    POETRY_CACHE_DIR=/home/user/.cache

RUN useradd -m user
USER user
WORKDIR /home/user/app

# Install poetry separated from system interpreter
RUN python3 -m venv $POETRY_VENV \
    && $POETRY_VENV/bin/pip install -U pip setuptools \
    && $POETRY_VENV/bin/pip install poetry==${POETRY_VERSION}

ENV PATH="${PATH}:/${POETRY_VENV}/bin"

COPY poetry.lock pyproject.toml /home/user/app/
RUN poetry install --no-interaction --no-root

COPY . /home/user/app

EXPOSE 80
CMD poetry run gunicorn core.wsgi -b 0.0.0.0:8000 --log-file -
