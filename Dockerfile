FROM python:3.7-alpine
MAINTAINER Paulo Fernandes

ENV PYTHONUNBUFFERED 1  #Recommended  when running Python within Docker containers. Doesnt allow Python to buffer the outputs.

COPY ./requirements.txt /requirements.txt
RUN apk add --update --no-cache postgresql-client jpeg-dev
RUN apk add --update --no-cache --virtual .tmp-build-deps \
    gcc libc-dev linux-headers postgresql-dev musl-dev zlib zlib-dev
RUN pip install -r requirements.txt
RUN apk del .tmp-build-deps

RUN mkdir /app
WORKDIR /app
COPY ./app app

RUN mkdir -p /vol/web/media
RUN mkdir -p /vol/web/static

RUN adduser -D user #Make sure the app is not run by the root account for satefy
RUN chown -R user:user /vol/
RUN chmod -R 755 /vol/web
USER user