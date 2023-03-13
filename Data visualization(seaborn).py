# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 19:55:09 2023

@author: AFSAR BASHA
"""

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

cars2 = pd.read_csv('Toyota.csv',index_col=0,na_values=["??","????"])

#Scatter plot
cars2.dropna(axis=0,inplace=True)
sns.set(style="darkgrid")
sns.regplot(x=cars2['Age'], y=cars2['Price'])
sns.regplot(x=cars2['Age'], y=cars2['Price'],fit_reg=False)
sns.regplot(x=cars2['Age'], y=cars2['Price'],marker="*",fit_reg=False)
sns.lmplot(x='Age', y='Price',data=cars2, fit_reg=False, hue='FuelType',legend=True,palette="Set1")

#Histogram
sns.displot(cars2['Age'])
sns.displot(cars2['Age'],kde=False,bins=5)

#BarPlot
sns.countplot(x="FuelType",data=cars2,hue="Automatic")

#Box and whiskers plot
sns.boxplot(y=cars2["Price"])
sns.boxplot(x=cars2['FuelType'],y=cars2["Price"])
sns.boxplot(x=cars2['FuelType'],y=cars2["Price"],hue="Automatic",data=cars2)

#Pairwise Plots

sns.pairplot(cars2, kind="scatter", hue="FuelType")
plt.show()






