# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 19:28:17 2018

@author: Francisco
"""
# Import csv file

# libraries
import matplotlib.pyplot as plt
from datetime import datetime as dt
import numpy as np
import pandas as pd
import seaborn as sns
import csv
from IPython import get_ipython

with open('blynkSensors.csv', 'r') as f:
  reader = csv.reader(f)
  csv_list = list(reader)

nr_data = len(csv_list)
csv_data=[]
for i in range(0,nr_data):
    csv_data.append(csv_list[i][0])
    
# data
df=pd.DataFrame({'x': range(0,nr_data), 'y': csv_data })
 
# plot
plt.plot(df.x,df.y)
plt.show()