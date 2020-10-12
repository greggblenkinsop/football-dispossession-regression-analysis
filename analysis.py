from sklearn import linear_model
import pandas as pd
import numpy as np
import statsmodels.api as sm
from analysismenu import analysismenu_print


def summary(v, f, d):
    data = pd.read_csv(d)
    ind_var = data[['Dispos']]
    dep_var = data[v]
    # FILTER IMPLEMENTATION TO DO
    filters = f
    x = sm.add_constant(dep_var)
    model = sm.OLS(ind_var, x).fit()
    print(model.summary())
    analysismenu_print(v, f, d)


def predict(v, f, d):
    data = pd.read_csv(d)
    ind_var = data[['Dispos']]
    dep_var = data[v]
    filters = f

    x = sm.add_constant(dep_var)
    model = sm.OLS(ind_var, x).fit()
    pred = model.predict(x)
    print(model.summary())
