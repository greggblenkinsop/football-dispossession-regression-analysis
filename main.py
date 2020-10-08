from sklearn import linear_model
import pandas as pd
import numpy as np
import statsmodels.api as sm
from menu import menu_print

variables = ['Age', 'Def 3rd', 'Mid 3rd', 'Att 3rd', '#Pl', 'Megs', 'PrgDist', 'Rec']
dataset = 'data.csv'




x =sm.add_constant(dep_var)
model = sm.OLS(ind_var,x).fit()
pred = model.predict(x)
print(model.summary())

def datasetchanger():
    menu_print()

def filterchanger():
    menu_print()

def runregression():
    data = pd.read_csv(dataset)
    ind_var = data[['Dispos']]
    dep_var = data[variables]

def printfilters():
    print(filters)

def printdataset():
    print(dataset)

def printvariables():
    print(variables)
