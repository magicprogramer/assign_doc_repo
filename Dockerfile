#base image
FROM python:3.8.2-slim-buster
COPY . /assignment2
WORKDIR /assignment2
CMD python cheeker.py