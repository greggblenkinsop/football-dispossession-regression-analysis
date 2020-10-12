def menu_print(v, f, d):
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
    if choice == 2:
        from main import filterchanger
        filterchanger()
    if choice == 3:
        from main import variablechanger
        variablechanger()
    if choice == 4:
        from analysismenu import analysismenu_print
        analysismenu_print(v, f, d)
