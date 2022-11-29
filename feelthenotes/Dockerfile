FROM python:3.9.15-alpine

WORKDIR /app

COPY . ./feelthenotes

RUN DEBIAN_FRONTEND=noninteractive TZ=Europe/Warsaw apt-get -y install tzdata

RUN pip install -r ./feelthenotes/requirements.txt
