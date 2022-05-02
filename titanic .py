
from cmath import nan
from itertools import count
from statistics import median
import numpy as np
import pandas as p
import seaborn as  s
import matplotlib.pyplot as plt
train=p.read_csv("train.csv")
print(train.isnull().sum())
train["Age"].plot(kind="hist")
train["Age"]=train.groupby(["Pclass","Sex"])["Age"].apply(lambda x:x.fillna(x.median()))

print("************************age replaced***************")
#a=train["Cabin"].unique()
train["Cabin"]=train["Cabin"].apply(lambda s :s[0]if p.notnull(s) else"M")
print("************************Cabin replaced***************")

a=train["Embarked"].isnull()
train["Embarked"][a==True]="S"
#print(train.isnull().sum())
print("************************Embarked replaced***************")
print(train.describe())
train.groupby(["Pclass","Sex"])["Age"].mean().plot(kind="bar")
plt.show()
train.groupby(["Pclass","Sex"])["Survived"].mean().plot(kind="bar")
plt.show()
train.groupby(["Sex"])["Age"].mean().plot(kind="bar")
plt.show()

