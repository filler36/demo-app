FROM python:3.9.15-alpine

ENV APP_DIR="./feelthenotes-app"

WORKDIR /app

COPY . $APP_DIR

RUN apk add --no-cache tzdata

ENV TZ=Europe/Warsaw

RUN pip install -r $APP_DIR/requirements.txt
