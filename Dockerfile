FROM python:3.11.7

ENV PYTHONUNBUFFERED 1

RUN mkdir /social_network

WORKDIR /social_network

COPY . /social_network/

RUN pip install -r requirements.txt


