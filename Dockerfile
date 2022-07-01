FROM python:3.10.4-slim-bullseye

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir /newsApp
RUN mkdir /newsApp/staticfiles
RUN mkdir /newsApp/media


WORKDIR /newsApp

RUN pip install --upgrade pip

COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY . .
