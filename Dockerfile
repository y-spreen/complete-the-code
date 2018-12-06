FROM ubuntu:18.04

RUN apt -y update
RUN apt -y install curl python2.7

RUN mkdir /code
WORKDIR /code

ADD run.sh .
ADD runfile.txt .
