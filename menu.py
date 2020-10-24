def menu_print(v, f, d):
    '''The function used to allow the user to navigate through the menu to alter the search settings
    
    Parameters:
    v (List): Variables that the analysis will be performed over
    f (List): Filters that will be performed over the dataset before the analysis
    d (String): The file name and location of the dataset to be analysed
    '''
    from main import printdataset, printfilters, printvariables
    ds = printdataset()
    fi = printfilters()
    va = printvariables()
    print("=============DATA=============\nCurrent Dataset:\n" + ds +
          "\nCurrent Filters:\n" + fi +
          "\nCurrent Variables:\n" + va +
          "\n=============MENU=============\n1 - Change Dataset\n2 - Change Filters\n3 - Change Variables\n4 - Run "
          "Regression Analysis")

    choice = int(input("============CHOICE============ \nInput - "))
  
    if choice == 1:
        from main import datasetchanger
        datasetchanger()
    elif choice == 2:
        from main import filterchanger
        filterchanger()
    elif choice == 3:
        from main import variablechanger
        variablechanger()
    elif choice == 4:
        from analysismenu import analysismenu_print
        analysismenu_print(v, f, d)
    else:
        print("INVALID INPUT")
        menu_print(v, f, d)
