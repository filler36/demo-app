FROM python:3.9.15-alpine

ENV APP_DIR="./feelthenotes-app"

WORKDIR /app

RUN apk add --no-cache tzdata

ENV TZ=Europe/Warsaw

COPY . $APP_DIR

RUN pip install --no-cache-dir -r $APP_DIR/requirements.txt