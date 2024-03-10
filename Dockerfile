# syntax=docker/dockerfile:1

FROM python:3.9.18-slim

WORKDIR /python-docker

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

# since we already have host in our app.py we can skip that argument
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0", "--port=5909"]
