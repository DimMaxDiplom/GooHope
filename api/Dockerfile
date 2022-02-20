FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONYNBUFFERED 1

WORKDIR /usr/src/api

COPY ./requirements.txt ./
RUN pip install -r ./requirements.txt

COPY . ./