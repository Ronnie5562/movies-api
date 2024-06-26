FROM python:3.9-alpine3.13
LABEL maintainer="Abimbola Ronald"
LABEL email="abimbolaaderinsola212@gmail.com"

#Makes the output of the python script to be unbuffered - makes you see your logs in real time
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /tmp/requirements.txt
COPY ./requirements.dev.txt /tmp/requirements.dev.txt
COPY ./app /app
WORKDIR /app
EXPOSE 8000

ARG DEV=false
RUN python -m venv /pyenv && \
    /pyenv/bin/pip install --upgrade pip && \
    apk add --update --no-cache postgresql-client jpeg-dev && \
    apk add --update --no-cache --virtual .tmp-build-deps \
        build-base postgresql-dev musl-dev zlib zlib-dev linux-headers && \
    /pyenv/bin/pip install -r /tmp/requirements.txt && \
    if [ $DEV = "true" ]; \
        then /pyenv/bin/pip install -r /tmp/requirements.dev.txt; \
    fi && \
    rm -rf /tmp && \
    apk del .tmp-build-deps && \
    adduser \
        --disabled-password \
        --no-create-home \
        django-user && \
    mkdir -p /vol/web/media && \
    mkdir -p /vol/web/static && \
    chown -R django-user:django-user /vol && \
    chmod -R 755 /vol

ENV PATH="/pyenv/bin:$PATH"
USER django-user