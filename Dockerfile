FROM python:3.10-alpine

WORKDIR /app

COPY ./requirements.txt ./

RUN pip install -r requirements.txt

CMD [ "python", "-m", "django" ]
CMD [ "python", "--version" ]
