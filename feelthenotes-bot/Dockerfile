FROM python:3.9.15-alpine

ENV APP_DIR="./feelthenotes-bot"

WORKDIR /app

COPY . $APP_DIR

RUN pip install -r $APP_DIR/requirements.txt
