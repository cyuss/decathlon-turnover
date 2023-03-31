FROM python:3.9-slim

# set work directory
WORKDIR /usr/src/tmp

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV	PYTHONUNBUFFERED 1
ENV	PIP_NO_CACHE_DIR=off
ENV	PIP_DISABLE_PIP_VERSION_CHECK=on
ENV	POETRY_VIRTUALENVS_IN_PROJECT=true
ENV	POETRY_NO_INTERACTION=1

# install system dependencies
RUN apt-get -y update && apt-get install -y libzbar-dev

# install poetry
RUN pip install poetry

COPY pyproject.toml ./
RUN poetry install

COPY ./decathlon_turnover ./decathlon_turnover
EXPOSE 5001

CMD poetry run uvicorn decathlon_turnover.main:app --host 0.0.0.0 --port 5001
