FROM python:3.8
ENV PYTHONUNBUFFERED 1
RUN mkdir /web
WORKDIR /web
COPY requirements.txt /web/
RUN pip install -r requirements.txt
COPY . /web/
WORKDIR ./src
