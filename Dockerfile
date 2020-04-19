FROM python:3.7

COPY requirements.txt /
RUN pip3 install -r /requirements.txt

COPY . /application
WORKDIR /application
