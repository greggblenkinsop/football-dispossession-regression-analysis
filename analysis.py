from sklearn import linear_model
import pandas as pd
import numpy as np
import statsmodels.api as sm
from analysismenu import analysismenu_print


def summary(v, f, d):
    '''
    Prints a summary of the regression analysis
    
    Parameters:
    v (List): Variables that the analysis will be performed over
    f (List): Filters that will be performed over the dataset before the analysis
    d (String): The file name and location of the dataset to be analysed
    
    '''
    data = pd.read_csv(d)
    ind_var = data[['Dispos']]
    dep_var = data[v]
    # FILTER IMPLEMENTATION TO DO
    filters = f
    x = sm.add_constant(dep_var)
    model = sm.OLS(ind_var, x).fit()
    print(model.summary())
    analysismenu_print(v, f, d)

#UNFINISHED FUNCTION
def predict(v, f, d):
    '''
    Allows the user to predict how often a player will be dispossessed based on the analysis
    
    Parameters:
    v (List): Variables that the analysis will be performed over
    f (List): Filters that will be performed over the dataset before the analysis
    d (String): The file name and location of the dataset to be analysed
    
    '''
    data = pd.read_csv(d)
    ind_var = data[['Dispos']]
    dep_var = data[v]
    filters = f

    x = sm.add_constant(dep_var)
    model = sm.OLS(ind_var, x).fit()
    pred = model.predict(x)
    print(model.summary())
