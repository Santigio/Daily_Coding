import math

# This is a simple Python calculator
Run = True

while Run:
    signs = int(input("press button (1=+), (2=-), (3=X), (4=/)"))
    User_input = int(input("Enter a number of your choice "))
    User_input1 = int(input("Enter a number of your choice "))


    def add(num1, num2):
        return num1 + num2


    def Sub(num1, num2):
        return num1 - num2



    def Multiply(num1, num2):
        return num1 * num2


    def Devision(num1, num2):
        return num1 / num2



    if signs == 1:
        print(User_input, "+", User_input1, "=",
        add(User_input, User_input1))
    elif signs == 2:
        print(User_input, "-", User_input1, "=",
        Sub(User_input, User_input1))
    elif signs == 3:
        print(User_input, "*", User_input1, "=",
        Multiply(User_input, User_input1))
    elif signs == 2:
        print(User_input, "/", User_input1, "=",
        Devision(User_input, User_input1))


    Exit = input("do you want to continue y/n")
    if Exit == "y":
        quit()