FROM python:3.9.15-alpine

WORKDIR /app

COPY . ./feelthenotes-app

RUN apk add --no-cache tzdata

ENV TZ=Europe/Warsaw

RUN pip install -r ./feelthenotes-app/requirements.txt
