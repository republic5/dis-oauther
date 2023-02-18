FROM python:3
USER root

COPY . /data

WORKDIR /data

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ENTRYPOINT []

CMD ["python3", "main.py"]
