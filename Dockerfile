FROM python:3.9.15-alpine

WORKDIR /app

COPY ./requirements.txt ./

COPY ./feelthenotes ./

COPY ./feelthenotes/feelthenotes/settings.py ./feelthenotes/feelthenotes/settings.py

RUN pip install -r requirements.txt

#RUN [ "django-admin", "startproject", "feelthenotes"]

CMD [ "python", "./feelthenotes/manage.py", "runserver", "0.0.0.0:8000" ]
