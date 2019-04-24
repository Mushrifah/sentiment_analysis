from flask import Flask, render_template, jsonify, request
from sklearn.externals import joblib
import traceback
import pandas as pd
import numpy as np
from sklearn.linear_model import SGDClassifier
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
global label_dictionary,svm,vectorizer
#vectorizer=TfidfVectorizer(ngram_range=(1, 1), min_df=0.0, max_df=1.0)
label_dictionary = {0: 'negative review', 1: 'positive review'}



app = Flask(__name__,)

@app.route("/")
def index():
    return render_template('form.html')

@app.route("/predict", methods=["POST"])
def predict():

    try:
            # json_ = request.json
		            
        query=[request.form.to_dict()['review']]
        # query1=vectorizer.transform(query)
        print(query)
        prediction = (svm.predict(vectorizer.transform(query)))
        print("#################################")
        print(prediction)
        return jsonify({'prediction': str(prediction),'label':label_dictionary[int(prediction)]})

    except:
        print(traceback.format_exc())
        return jsonify({'trace': traceback.format_exc()})
  







if __name__ == '__main__':

    try:
        port = int(sys.argv[1]) # This is for a command-line input
    except:
        port = 12345 # If you don't provide any port the port will be set to 12345





    svm = joblib.load("svm_classifier.pkl") # Load "model.pkl"
    print ('Model loaded')
    vectorizer=joblib.load("vectorizer.pkl")
    
    app.run(port=port, debug=False)


 











