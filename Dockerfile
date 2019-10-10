FROM python:latest
RUN mkdir /service
WORKDIR /service
ADD requirements.txt /service
RUN pip install -r requirements.txt
ADD . /service


