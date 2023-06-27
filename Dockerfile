FROM ubuntu:latest
RUN apt-get update -qy
RUN apt-get install -qy python3 python3-pip
COPY ./src /app
WORKDIR /app
CMD ["python3", "main.py"]