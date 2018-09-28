# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd
import statsmodels.api as sm
from sklearn.linear_model import LinearRegression
from sklearn.feature_selection import RFE
import matplotlib.pyplot as plt
import seaborn as sns
from pandas.plotting import scatter_matrix
from pandas import set_option
from pandas import read_csv
import numpy as np
import seaborn as sns

filename = 'Avibase_bird_species.csv'
data = read_csv(filename, engine='python')


def updateCSV(df, filepath):
    with open(filepath, 'w') as f:
             df.to_csv(f, header=True, index = False)             

def cleaningData(df):
    for index, row in df.iterrows():
        data.at[index, 'name'] = row['name'].lower()
        print(row['name'].lower())
        
    df.drop_duplicates(keep=False, inplace=True)
    
    updateCSV(df,filename)



cleaningData(data)
