FROM python:3.11.4

ENV APP_HOME /app
WORKDIR $APP_HOME

COPY . .

RUN ["pip3", "install", "-r", "requirements.txt"]

ENV PORT 8080
CMD exec gunicorn --bind 0.0.0.0:$PORT --workers 2 --threads 4 --timeout 0 wsgi:app
