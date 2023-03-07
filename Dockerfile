FROM python:3.11.2-slim

# RUN apt-get update \
#     && apt-get upgrade -y \
#     && apt-get install -y --no-install-recommends curl git build-essential python3-setuptools \
#     && apt-get autoremove -y

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN adduser --disabled-password --gecos '' appuser
WORKDIR /server

RUN pip install --upgrade pip
RUN pip install poetry

COPY pyproject.toml poetry.lock ./
RUN poetry export --without-hashes --without dev -f requirements.txt -o requirements.txt && \
        chown appuser:appuser requirements.txt && \
        pip install -r requirements.txt

USER appuser
COPY --chown=appuser:appuser start.sh /server/
COPY --chown=appuser:appuser app /server/app

RUN chmod +x /server/start.sh
ENTRYPOINT [ "/server/start.sh" ]
