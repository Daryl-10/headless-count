# Use the official Python image.
# https://hub.docker.com/_/python

FROM python:3.9-slim

RUN apt-get update && apt-get install -y libglib2.0-0 libgl1-mesa-glx libsm6 && rm -rf /var/lib/apt/lists/*

# Install Python dependencies.
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copy local code to the container image.
ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . .


CMD [ "python", "./isolate.py"]