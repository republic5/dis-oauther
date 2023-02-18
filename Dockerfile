FROM python:3
USER root

RUN pip install --upgrade pip
RUN pip install -r requirements.txt