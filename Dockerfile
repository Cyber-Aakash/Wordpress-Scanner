FROM python:latest

WORKDIR /app

COPY wpscanner.py ./

CMD [ "python", "./wpscanner.py"]