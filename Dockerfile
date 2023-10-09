FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /doc
COPY ./requirements.txt /doc
RUN pip install -r /doc/requirements.txt
COPY quality /doc
EXPOSE 8000
