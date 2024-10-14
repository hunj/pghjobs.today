FROM python:3.11

ENV LANGUAGE C.UTF-8
ENV LC_ALL C.UTF-8

ENV PYTHONHASHSEED 1
ENV PYTHONUNBUFFERED 1

ARG NODE_MAJOR=20

RUN apt-get update && apt-get install -y \
    bash-completion \
    curl \
    less \
    libpq-dev \
    netcat-traditional \
    vim

RUN pip install --upgrade pip
RUN pip install poetry
COPY ./pyproject.toml ./
COPY ./poetry.lock ./

# Install Poetry packages without a virtualenv in container
RUN poetry config virtualenvs.create false && \
    poetry install --no-root

COPY app /app
RUN mkdir -p /app/static
WORKDIR /app

CMD bin/boot.sh
