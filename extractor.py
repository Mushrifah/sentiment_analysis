# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 21:14:25 2019

@author: mushrifah
"""

import os
import pandas as pd
import numpy as np

labels = {'pos': 'positive', 'neg': 'negative'}

dataset = pd.DataFrame()
for directory in ('test', 'train'):
    for sentiment in ('pos', 'neg'):
        path =r'F:/aclImdb/{}/{}'.format(directory, sentiment)
        for review_file in os.listdir(path):
            with open(os.path.join(path, review_file), 'r',encoding="utf8") as input_file:
                review = input_file.read()
            dataset = dataset.append([[review, labels[sentiment]]], 
                                     ignore_index=True)

dataset.columns = ['review', 'sentiment']

indices = dataset.index.tolist()
np.random.shuffle(indices)
indices = np.array(indices)

dataset = dataset.reindex(index=indices)

dataset.to_csv('movie_reviews.csv', index=False,encoding="utf8")