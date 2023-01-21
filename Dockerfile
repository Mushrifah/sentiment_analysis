# set base image (host OS)

FROM python:3.9.12

# set the working directory in the container

# this is path to folder where all project contents are stored

# i.e. flask file, model pickle files, Dockerfile, requirements.txt

WORKDIR D:/projects/sentiment_analysis

# copy the dependencies file to the working directory

COPY requirements.txt .

# install dependencies

RUN pip install -r requirements.txt

# copy the content of the directory to the working directory

COPY . .

# command to run on container start

# main cmd to start the flask server

CMD [ "python", "./app.py" ]