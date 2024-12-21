FROM python:3.11.11-alpine3.21

LABEL org.opencontainers.image.authors="abudulin@foxmail.com"

WORKDIR /app
COPY . /app

ENV DOCKER=1

ARG CN=false
RUN if [ "$CN" = "true" ]; then \
        pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple/ && \
        pip config set global.trusted-host pypi.tuna.tsinghua.edu.cn; \
    fi

RUN apk add --no-cache build-base

RUN python -m pip install --upgrade pip && \
    pip install -r requirements-slim.txt && \
    chmod +x /app/entrypoint.sh

EXPOSE 8000

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    DOCKER=1 \
    WORKERS=4 \
    THREADS=4 \
    TIMEOUT=600

ENTRYPOINT ["/app/entrypoint.sh"]