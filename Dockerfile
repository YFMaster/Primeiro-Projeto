FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# Instala o Poetry
RUN pip install --no-cache-dir poetry

# Copia definições de dependências
COPY mydjangoapp/pyproject.toml ./

# Instala dependências do projeto
RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi

# Copia o restante do código
COPY mydjangoapp/ ./

CMD ["gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8000"]
