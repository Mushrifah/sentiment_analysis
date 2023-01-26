from flask import Flask, render_template, jsonify, request
import pickle
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

  
    port = 5000 # If you don't provide any port the port will be set to 12345


    #load the model
    svm_pkl=open('svm_classifier.pkl','rb')
    svm=pickle.load(svm_pkl)

    #load the vectorizer model
    vectorizer_pkl=open('vectorizer.pkl','rb')
    vectorizer=pickle.load(vectorizer_pkl)
    

    
    app.run(host='0.0.0.0',port=port, debug=False)


 











