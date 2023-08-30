# pull official base image
FROM python:3.9-slim-buster

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory
WORKDIR /app

# install dependencies
COPY ./requirements.txt /app

RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

# copy project
COPY . /app

# Run the Django app
CMD sh -c "python manage.py makemigrations && python manage.py migrate && python manage.py runserver 0.0.0.0:8000"