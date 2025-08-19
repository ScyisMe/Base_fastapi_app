FROM python:3.13-slim AS builder

WORKDIR /FastapiBse

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libffi-dev \
    curl \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir poetry

COPY pyproject.toml poetry.lock ./

RUN poetry config virtualenvs.in-project true \
    && poetry install --no-interaction --no-ansi

COPY fastapi-application ./fastapi-application

FROM python:3.13-slim 

WORKDIR /FastapiBse

COPY --from=builder /FastapiBse/fastapi-application ./fastapi-application
COPY --from=builder /FastapiBse/.venv ./.venv

ENV PATH="/FastapiBse/.venv/bin:$PATH"
ENV PYTHONUNBUFFERED=1

WORKDIR /FastapiBse/fastapi-application

EXPOSE 8080

CMD ["uvicorn", "main:main_app", "--host", "0.0.0.0", "--port", "8080"]