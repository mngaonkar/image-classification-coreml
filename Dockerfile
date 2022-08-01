FROM ubuntu:20.04

RUN mkdir app
COPY *.py app/
COPY requirements.txt app/ 
WORKDIR app
RUN apt-get update
RUN apt-get -y install python3 python3-pip 
RUN pip3 install -r requirements.txt
