FROM python:3.9.15-alpine

RUN apk add --no-cache tzdata
ENV TZ=Europe/Warsaw

ENV APP_DIR="./feelthenotes-app"

WORKDIR /app

COPY . $APP_DIR

RUN pip install --no-cache-dir -r $APP_DIR/requirements.txt