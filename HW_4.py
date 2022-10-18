# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 20:46:21 2022

@author: Mohd Ariz Khan
"""

#=========================================================    
# step1: import the data files and libraires
import pandas as pd
df = pd.read_csv("Advertising.csv")
df.shape
df.head()
#=========================================================    

# step2: split the Variables in  X and Y's
#m1
X = df[["TV"]]

#m2
X = df[["TV","radio"]]

#m3
X = df[["TV","radio","newspaper"]]

#m4
X = df[["TV","radio","newspaper","ID"]]

# Target
Y = df["sales"]

#=========================================================    

# scatter plot between each x and Y
import matplotlib.pyplot as plt
plt.scatter(df.iloc[:,0], Y, color='red')
plt.ylabel("sales")
plt.xlabel("ID")
plt.show()

import matplotlib.pyplot as plt
plt.scatter(df.iloc[:,1], Y, color='pink')
plt.ylabel("sales")
plt.xlabel("TV")
plt.show()

import matplotlib.pyplot as plt
plt.scatter(df.iloc[:,2], Y, color='blue')
plt.ylabel("sales")
plt.xlabel("radio")
plt.show()

import matplotlib.pyplot as plt
plt.scatter(df.iloc[:,3], Y, color='orange')
plt.ylabel("sales")
plt.xlabel("newspaper")
plt.show()

# correlation
df.corr()

# Model fitting --> Scikit learn
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score 
import numpy as np

LR = LinearRegression()
LR.fit(X,Y)
Y_pred = LR.predict(X)
mse= mean_squared_error(Y,Y_pred)
RMSE = np.sqrt(mse)
print("Root mean squarred error: ", RMSE.round(3))
print("Rsquare: ",r2_score(Y,Y_pred).round(3)*100)