FROM python:3.9.15-alpine

WORKDIR /app

COPY ./requirements.txt ./

RUN pip install -r requirements.txt

CMD [ "python", "-m", "django" ]
