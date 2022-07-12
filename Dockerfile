FROM python:3.9.13

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt requirements.txt 

RUN  pip install --upgrade pip \
     && pip install -r requirements.txt 


COPY . /app/

RUN DJANGO_SETTINGS_MODULE=url_shorter.settings.prod \
    SECRET_KEY=TEST_SECRET_KEY

EXPOSE $PORT

RUN ["chmod", "+x", "/app/entrypoint-prod.sh"]
ENTRYPOINT ["/app/entrypoint-prod.sh"]



