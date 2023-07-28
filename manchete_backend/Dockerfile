FROM python:3.8-slim

ENV PYTHONUNBUFFERED 1

RUN mkdir -p /app

COPY . /app

RUN apt-get update
RUN apt-get install python3-dev default-libmysqlclient-dev gcc  -y

WORKDIR /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD [ "python", "/app/manage.py", "runserver", "0.0.0.0:8000" ]
