# -*- coding: utf-8 -*-
"""
Created on Sat Oct  1 11:16:36 2022

@author: ADMIN
"""

import pandas as pd
df = pd.read_csv("F:\\ExcelR\\data\\tips.csv")
df

df.head()
df.dtypes

#==============================================
#Box plot for all numerical variables
df.boxplot(column='total_bill',vert=False)

import seaborn as sns
sns.boxplot(x='total_bill', data=df, color='red')
sns.boxplot(x='tip', data=df, color='blue')
sns.boxplot(x='sex', data=df, color='green')
sns.boxplot(x='smoker', data=df, color='yellow')
sns.boxplot(x='day', data=df, color='orange')
sns.boxplot(x='time', data=df, color='purple')
sns.boxplot(x='size', data=df, color='pink')

#=================================================
#Histogram
df["total_bill"].hist(color="red")
df["total_bill"].skew()
df["total_bill"].kurt()

df["tip"].hist(color="blue")
df["tip"].skew()
df["tip"].kurt()

df["sex"].hist(color="green")
df["sex"].skew()
df["sex"].kurt()

df["smoker"].hist(color="yellow")
df["smoker"].skew()
df["smoker"].kurt()

df["day"].hist(color="orange")
df["day"].skew()
df["day"].kurt()

df["time"].hist(color="purple")
df["time"].skew()
df["time"].kurt()

df["size"].hist(color="pink")
df["size"].skew()
df["size"].kurt()

#==================================================
#scatter plot
df.plot.scatter("total_bill","tip")

df[["total_bill","tip"]].corr()

import matplotlib.pyplot as plt
plt.scatter(x = df["total_bill"], y = df["tip"], color="red")
plt.show()

plt.scatter(x = df["sex"], y = df["tip"], color="blue")
plt.show()

plt.scatter(x = df["sex"], y = df["smoker"], color="green")
plt.show()

plt.scatter(x = df["smoker"], y = df["tip"], color="orange")
plt.show()

plt.scatter(x = df["total_bill"], y = df["time"], color="pink")
plt.show()

plt.scatter(x = df["size"], y = df["time"], color="black")
plt.show()

plt.scatter(x = df["time"], y = df["day"], color="purple")
plt.show()

#========================================================
#Bar Plot
df.dtypes

t1 = df["smoker"].value_counts()
t1
t1.plot(kind='bar', color='red')
t1.plot(kind='pie')

#========================================================
#g1 = df.groupby("time")
#g1.sum()

t2 = pd.crosstab(index = df["sex"], columns = df["day"])
print(t2)
t2.plot(kind='bar', figsize=(12,6))

# case 1
df_sex =df[(df['sex'] == "Male") | 
   (df['sex'] == "Female")]

# case 2
df_day =df[(df['day'] == "Sun") | 
   (df['day'] == "Sat") | 
   (df['day'] == "Fri") |
   (df['day'] == "Thur") |
   (df['day'] == "mon") |
   (df['day'] == "Tues") |
   (df['day'] == "Wed")]

#=======================================================
#Stacked bar chart
t2 = pd.crosstab(index = df["day"], columns = df["sex"])
print(t2)
t2.plot(kind='bar', figsize=(10,5))




























