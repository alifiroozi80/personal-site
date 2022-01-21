FROM python:3.9-alpine

RUN apk update

WORKDIR /website

COPY requirements.txt /website

RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python3", "main.py"]
