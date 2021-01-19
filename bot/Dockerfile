# pull official base image
FROM python:3.9-alpine

# set work directory
WORKDIR /usr/src/bot

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies
RUN apk update \
    && apk add gcc python3-dev musl-dev libc-dev libffi-dev openssl-dev libxml2-dev libxslt-dev

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/bot/requirements.txt
RUN pip install -r requirements.txt

# copy project
COPY . /usr/src/bot/