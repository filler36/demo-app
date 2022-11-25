FROM python:3.9.15-alpine

WORKDIR /app

COPY ./requirements.txt ./

COPY ./feelthenotes ./feelthenotes

RUN pip install -r requirements.txt
