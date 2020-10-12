def analysismenu_print(v, f, d):
    print(
        "=============MENU=============\n1 - Regression Analysis Summary\n2 - Predict a Players Dispossession "
        "Value\n3 - Change Data")
    choice = int(input("============CHOICE============ \nInput - "))

    if choice == 1:
        from analysis import summary
        summary(v, f, d)
    if choice == 2:
        from analysis import predict
        predict(v, f, d)
