FROM python:3-slim

WORKDIR /programas/ingesta

RUN pip3 install boto3 pandas mysql-connector-python

COPY . .

CMD [ "python3", "./ingesta.py" ]
