FROM python:3.8.16-slim

ENV PYTHONBUFFERED 1

RUN mkdir /portfolio

WORKDIR /portfolio

COPY . .

RUN pip install -r requirements.txt