FROM python:3-slim-buster

WORKDIR app

RUN pip install pipenv

COPY Pipfile Pipfile
COPY Pipfile.lock Pipfile.lock

COPY hw16.py hw16.py

CMD python hw16.py
