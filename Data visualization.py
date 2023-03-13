# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 19:32:05 2023

@author: AFSAR BASHA
"""

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

cars2 = pd.read_csv('Toyota.csv',index_col=0,na_values=["??","????"])

cars2.dropna(axis=0,inplace=True)

#Scatter Plot
plt.scatter(cars2['Age'],cars2['Price'],c='red')
plt.title('Scatter plot of price vs Age of cars')
plt.xlabel('Age (months)')
plt.ylabel('Price (Euros')
plt.show()

#Histogram

plt.hist(cars2['KM'])
plt.show()

#Histogram 2

plt.hist(cars2['KM'],color='green',edgecolor='white',bins=5)
plt.title("Histo of Kms")
plt.xlabel('Kms')
plt.ylabel('Frequency')
plt.show()

#Bar Plot

counts = [979, 120, 12]
fuelType=('Petrol','Diesel','CNG')
index = np.arange(len(fuelType))

plt.bar(index, counts, color=['red','green','blue'])
plt.title('Bar plot of fuel Types')
plt.xlabel('Fuel Types')
plt.ylabel('Frequency')
plt.show()

plt.xticks(index, fuelType,rotation = 90)
plt.show()



























