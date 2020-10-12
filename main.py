from sklearn import linear_model
import pandas as pd
import numpy as np
import statsmodels.api as sm
import menu

variables = ['Age', 'Def 3rd', 'Mid 3rd', 'Att 3rd', '#Pl', 'Megs', 'PrgDist', 'Rec']
filters = []
dataset = 'data.csv'


def datasetchanger():
    global dataset
    dataset = input("=============DATA=============" +
                    "\nPlease enter the relative location and file name:\n"
                    )
    menu.menu_print(variables, filters, dataset)


def filterchanger():
    global filters
    filter_var = input("============FILTER============" +
                       "\nPlease enter the filtered variable from the following:" +
                       "\n" + ' - '.join(variables) + "\n"
                       )
    if filter_var in variables:
        filter_eq = input("\nPlease enter the equation for" + filter_var + "below as follows (== 6, > 23, etc):\n")
        filter_fin = filter_var + " " + filter_eq
        filters.append(filter_fin)
        menu.menu_print(variables, filters, dataset)
    else:
        print("===========WARNING============" +
              "\nInvalid inputted variable"
              )
        menu.menu_print(variables, filters, dataset)


def variablechanger():
    global variables
    vc_choice = input("===========VARIABLE===========" +
                      "\nTo see possible variables view: " + dataset +
                      "\nCurrent Variables: " + ' - '.join(variables) +
                      "\n\nTo add or remove a variable type it as its spelled above, if complete leave blank:\n"
                      )
    if vc_choice == "":
        menu.menu_print(variables, filters, dataset)
    else:
        if vc_choice in variables:
            variables.remove(vc_choice)
        elif vc_choice in pd.read_csv(dataset).iloc[0]:
            variables.append(vc_choice)
        else:
            print("Invalid Variable")
        variablechanger()


def printfilters():
    return ' - '.join(filters)


def printdataset():
    return ''.join(dataset)


def printvariables():
    return ' - '.join(variables)


menu.menu_print(variables, filters, dataset)
