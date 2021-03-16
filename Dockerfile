FROM python:3.9.1-alpine

WORKDIR /usr/src/app

COPY . .

CMD ["python", "./b.py"]