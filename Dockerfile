# pull from official base image
FROM python:3.7.4-alpine

# install environtment depedencies
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev

# set working directory
WORKDIR /usr/src/app

#set environtment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# add and install requirements
COPY ./requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# add entrypoint.sh
COPY ./entrypoint.sh .

# add app
COPY . .

# run server
CMD ["./entrypoint.sh"]
