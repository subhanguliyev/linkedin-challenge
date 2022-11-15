FROM python:3.10.4-alpine
WORKDIR /linkedin-challenge
COPY . /linkedin-challenge
RUN /usr/local/bin/python -m pip install --upgrade pip
RUN apk update && pip install -r /linkedin-challenge/requirements.txt --no-cache-dir
EXPOSE 8080
CMD ["python", "main.py", "-d"]