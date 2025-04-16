FROM python:3.13-slim
ENV POETRY_VIRTUALENVS_CREATE=false

WORKDIR app/
COPY . .

RUN pip install poetry
RUN pip install greenlet
RUN apt-get update && apt-get install -y build-essential libpq-dev curl

RUN poetry config installer.max-workers 10
RUN poetry install --no-interaction --no-ansi
RUN poetry add "psycopg[binary]"

EXPOSE 8000
CMD poetry run uvicorn --host 0.0.0.0 fast_zero.app:app