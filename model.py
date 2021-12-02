# Ref: https://medium.com/analytics-vidhya/deploying-a-machine-learning-model-as-a-flask-app-on-heroku-part-1-b5e194fed16d

import pandas as pd
import numpy as np
import pickle

from sklearn.datasets import load_wine
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

wine = load_wine()

data = pd.DataFrame(data= np.c_[wine['data'], wine['target']],
                     columns= wine['feature_names'] + ['target'])


X = data.iloc[:, :-1]
y = data.iloc[:, -1]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=0)


clf = LogisticRegression()
clf = clf.fit(X_train,y_train)
y_pred = clf.predict(X_test)
print("accuracy_score: %.2f" % accuracy_score(y_test, y_pred))


path='./lib/models/LogisticRegression.pkl'
with open(path, 'wb') as file:
    pickle.dump(clf, file)

