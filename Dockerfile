FROM python:3
USER root

RUN pip install --upgrade pip
RUN pip install discord.py==2.1.0
RUN pip install Flask==2.2.2
RUN pip install requests==2.28.2
RUN pip install PyYAML==6.0
