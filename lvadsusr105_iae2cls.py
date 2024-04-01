# -*- coding: utf-8 -*-
"""LVADSUSR105_IAE2CLS.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1yiVEPPpjPJSq-UR3BpMItLZnKbxk6_02
"""

import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.model_selection  import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score , precision_score, recall_score, f1_score, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

data  = pd.read_csv("/content/drive/MyDrive/Mall_Customers.csv")
ndf = pd.DataFrame(data)

nullcount=ndf.isnull().sum()

print(nullcount)

ndf.fillna(ndf.mean(),inplace =True)

nullcount1=ndf.isnull().sum()

print(nullcount1)


q1  =ndf.quantile(0.25)
q3  =ndf.quantile(0.75)
iqr  = q3-q1
outlier  = ((ndf<(q1-iqr*1.5)) | (ndf>(q3+iqr*1.5))).any(axis=1)
fdf = ndf[~outlier]

plt.figure(figsize=(10,7))
sns.boxplot(fdf)
plt.show()

ndf["Income to spending ratio"] = (ndf["Annual Income (k$)"]/ndf["Spending Score (1-100)"])*100
ndf

encoder  = LabelEncoder()
ndf["Gender"] = encoder.fit_transform(ndf["Gender"])

model = KMeans(n_clusters=8)

op = model.fit_predict(ndf)

print("Targerted Strategise")
print("On seeing the cluster it is clear that one who earns more spends more ,therefore target the people who earns more")