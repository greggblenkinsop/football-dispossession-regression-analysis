from main import datasetchanger, filterchanger, runregression, printdataset, printfilters


def menu_print():
    choice = input("=============DATA=============" +
                   "\nCurrent Dataset:\n" + printdataset() +
                   "\nCurrent Filters:\n" + printfilters() +
                   "\n\n=============MENU=============" +
                   "\n1 - Change Dataset" +
                   "\n2 - Change Filters" +
                   "\n3 - Run Regression Analysis"
                   "\n\n============CHOICE============" +
                   "\nInput - "
                   )
    if choice == 1:
        datasetchanger()
    if choice == 2:
        filterchanger()
    if choice == 3:
        runregression()
