FROM python:3.9.15-alpine

WORKDIR /app

COPY ./requirements.txt ./

#RUN pip install -r requirements.txt

CMD [ "python", "-m", "pip", "install", "django" ]

CMD [ "django-admin", "startproject", "feelthenotes"]

CMD [ "python", "./feelthenotes/manage.py", "runserver" ]
