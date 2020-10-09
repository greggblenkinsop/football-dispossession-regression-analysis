from sklearn import linear_model
import pandas as pd
import numpy as np
import statsmodels.api as sm
import menu

variables = ['Age', 'Def 3rd', 'Mid 3rd', 'Att 3rd', '#Pl', 'Megs', 'PrgDist', 'Rec']
dataset = 'data.csv'
filters = []


def datasetchanger():
    global dataset
    dataset = input("=============DATA=============" +
                    "\nPlease enter the relative location and file name:\n"
                    )
    menu.menu_print()


def filterchanger():
    global filters
    filter_var = input("============FILTER============" +
                       "\nPlease enter the filtered variable from the following:" +
                       "\n" + ''.join(variables)
                       )
    if filter_var in variables:
        filter_eq = input("\nPlease enter the equation for" + filter_var + "below as follows (== 6, > 23, etc):\n")
        filter = filter_var + " " + filter_eq
        filters.append(filter)
        menu.menu_print()
    else:
        print("===========WARNING============" +
              "\nInvalid inputted variable"
              )
        menu.menu_print()


def variablechanger():
    global variables
    menu.menu_print()


def runregression(d, v, f):
    data = pd.read_csv(d)
    ind_var = data[['Dispos']]
    dep_var = data[v]
    filters = f

    x = sm.add_constant(dep_var)
    model = sm.OLS(ind_var, x).fit()
    pred = model.predict(x)
    print(model.summary())


def printfilters():
    return ''.join(filters)


def printdataset():
    return ''.join(dataset)


def printvariables():
    return ' - '.join(variables)


menu.menu_print()
