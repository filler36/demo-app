FROM python:3.9.15-alpine

WORKDIR /app

COPY . ./feelthenotes

ENV DEBIAN_FRONTEND="noninteractive" TZ="Europe/Warsaw"

RUN DEBIAN_FRONTEND=$DEBIAN_FRONTEND TZ=$TZ apt-get -y install tzdata

RUN pip install -r ./feelthenotes/requirements.txt
