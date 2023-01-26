# Sentiment Analysis on IMDB reviews dataset
A flask app for predicting sentiment of movie reviews trained on imdb movie reviews dataset 



# Steps to run the project

1. Clone the repository

2. Create a virtual conda environment with `conda create -n sentiment python=3.9` and activate the env with `conda activate sentiment`.

3. Install the necessary packages with `pip insatll -r requirements.txt`

4. Run python app.py to view the final webpage

# Run from docker:

1. Change the Dockerfile by changing the `WORKDIR` to your own path where project files are stored

2. Build the Dockerfile on cmd as: `docker build . -t sentiment`

3. Once the image is downloaded run a container as: `docker run -d --name sentiment -p 5000:5000 sentiment`

4. Now you have a docker container named sentiment running.

5. Go to `localhost:5000` to view the sentiment analysis web application
 





