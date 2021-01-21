def position():
    while True:
        user = int(input("What index position do you want to know?: "))
        arr = [1, 2, 3, 4, 5, 6, 7, 8]
        x = []
        for i in range(len(arr)):
            if user == i:
                x.append(i - 1)
                print("The index position of", user, "is :", x)
        cont = input("do you still want to continue :")
        if cont == "yes":
            continue
        else:
            print("See you later!")
            quit()





position()
