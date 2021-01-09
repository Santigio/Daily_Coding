
Run = True
Exit = False

while Run:
    button = int(input("Press 1(add), 2(subtract), 3(divide), 4(multiply)"))
    User_input = int(input("Enter a number "))
    User_input1 = int(input("Enter another number "))




    def Addition(user1, user2):
        return user1 + user2


    def Subtration(user1, user2):
        return user1 - user2


    def Division(user1, user2):
        return user1 / user2


    def Multiplication(user1, user2):
        return user1 * user2


    if button == 1:
        print(User_input, "+", User_input1, "=",
              Addition(User_input, User_input1))
    elif button == 2:
        print(User_input, "-", User_input1, "=",
              Subtration(User_input, User_input1))
    elif button == 3:
        print(User_input, "/", User_input1, "=",
              Division(User_input, User_input1))
    elif button == 4:
        print(User_input, "*", User_input1, "=",
              Multiplication(User_input, User_input1))


    Question = input("Do you still want to continue? ")
    if Question == "n" or "no":
        quit()
    else:
        if Question == "yes" or "y":
            continue

