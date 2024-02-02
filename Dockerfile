FROM python:3.11.2-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /server

RUN pip install --upgrade pip
RUN pip install poetry

COPY pyproject.toml poetry.lock ./
RUN poetry export --without-hashes --without dev -f requirements.txt -o requirements.txt && \
        pip install -r requirements.txt

COPY . .

RUN chmod +x /server/start.sh
ENTRYPOINT [ "/server/start.sh" ]
