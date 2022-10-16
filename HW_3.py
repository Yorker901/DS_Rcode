# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 22:30:31 2022

@author: Ariz Aslam Khan
"""
import pandas as pd

df = pd.read_csv("F:\\ExcelR\\data\\market.csv")
df

df["Region"].value_counts()
n1 = 62
n2 = 14

# western Europe total returns
df1 = df[df["Region"] == 'Western Europe']
df1['Returns'].sum()

# asia total returns
df2 = df[df["Region"] == 'Asia']
df2['Returns'].sum()

# total returns
df['Returns'].sum()

p1 = df1['Returns'].sum() / df['Returns'].sum()
p1

p2 = df2['Returns'].sum() / df['Returns'].sum()
p2

prop = np.array([p1*100, p2*100])
samplesize = np.array([62, 14])

from statsmodels.stats.proportion import proportions_ztest

stats, pval = proportions_ztest(prop, samplesize)

alpha = 0.5

if pval<alpha:
    print("H0 is rejected and H1 is accepted")
else:
    print("H1 is rejected and H0 is accepted")
    
#=======================================================
import numpy as np

df["Product"].value_counts()
m1 = 52
m2 = 51

dg = df[df["Product"] == 'Boot']
dg['Sales'].sum()

dh = df[df["Product"] == 'Sport Shoe']
dh['Sales'].sum()

df['Sales'].sum()

p1 = dg['Sales'].sum() / df['Sales'].sum()
p1

p2 = dh['Sales'].sum() / df['Sales'].sum()
p2

prop = np.array([p1*100, p2*100])
samplesize = np.array([51, 51])

from statsmodels.stats.proportion import proportions_ztest

stats, pval = proportions_ztest(prop, samplesize)

alpha = 0.5

if pval<alpha:
    print("H0 is rejected and H1 is accepted")
else:
    print("H1 is rejected and H0 is accepted")