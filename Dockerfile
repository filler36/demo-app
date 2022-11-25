FROM python:3.9.15-alpine

WORKDIR /app

COPY ./requirements.txt ./

COPY ./feelthenotes ./feelthenotes

RUN pip install -r requirements.txt

CMD [ "python", "./feelthenotes/manage.py", "migrate", "&&", "python", "./feelthenotes/manage.py", "runserver", "0.0.0.0:8000"]
