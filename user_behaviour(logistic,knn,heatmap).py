# -*- coding: utf-8 -*-
"""user_behaviour(logistic,knn,heatmap).ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/160DTK7KSkhCabvlgT4DDJRIVaXd0T-4G
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

path='/content/user_behavior_dataset.csv'
data=pd.read_csv(path)
data.head()

from sklearn import preprocessing
le = preprocessing.LabelEncoder()
data['Gender'] = le.fit_transform(data['Gender'])
data['Device Model'] = le.fit_transform(data['Device Model'])
data['Operating System'] = le.fit_transform(data['Operating System'])
# print(data)

x = data[['Gender','Device Model','Operating System','App Usage Time (min/day)','Screen On Time (hours/day)','Battery Drain (mAh/day)','Number of Apps Installed','Data Usage (MB/day)','Age']].values
y = data['User Behavior Class'].values

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.20,random_state=0)
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(x_train,y_train)
y_pred = knn.predict(x_test)
# print(y_pred)
# print(y_test)

from sklearn import metrics
print("accuracy:",metrics.accuracy_score(y_test,y_pred))

from sklearn import metrics
cnf_matrix = metrics.confusion_matrix(y_test,y_pred)
print(cnf_matrix)

# Commented out IPython magic to ensure Python compatibility.
import seaborn as sns
# %matplotlib inline
class_names= [0,1]
fig,ax = plt.subplots()
tick_marks = np.arange(len(class_names))
plt.xticks(tick_marks,class_names)
plt.yticks(tick_marks,class_names)
print
# create headmap
sns.heatmap(pd.DataFrame(cnf_matrix),annot=True,cmap="Greens",fmt="d",annot_kws={"size":10})
ax.xaxis.set_label_position("bottom")
plt.tight_layout()
plt.title("confusion matrix", y=1.4)
plt.xlabel('actual label')
plt.xlabel('predicted label')

#import the class
from sklearn.linear_model import LogisticRegression
#instantiate the model(using the default parameters)
logreg=LogisticRegression()
#fit the model with data
logreg.fit(x_train,y_train)
print(y_test)
y_pred= logreg.predict(x_test)
print(y_pred)

from sklearn import metrics
print("accuracy:",metrics.accuracy_score(y_test,y_pred))