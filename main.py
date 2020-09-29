from sklearn import linear_model
import pandas as pd
import numpy as np


dataset = 'data.csv'
data = pd.read_csv(dataset)
ind_var = data[['Dispos']]
dep_var = data[['Age', '#Pl']]

regr = linear_model.LinearRegression()
regr.fit(dep_var, ind_var)

