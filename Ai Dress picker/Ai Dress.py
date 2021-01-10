
dress_store = ["Casual Dress Code", "Smart Casual Dress Code", "Business Casual Dress Code",
               "Cocktail Attire Dress Code"]
Run = True
while Run:
    ask_question = int(input("How happy are you? button= (1=100), (2=50), (3=10)"))
    ask_question2 = int(input("How intelligence you feel? button= (1=100), (2=50), (3=10)"))
    ask_question3 = int(input("How serious you are? button= (1=100), (2=50), (3=10)"))
    try:
        if ask_question & ask_question2 & ask_question3 == 1 & 1 & 1:
            for dresses in dress_store:
                print("The best dress for you today is ", dress_store[2])
                break
        if ask_question & ask_question2 & ask_question3 == 2 & 2 & 2:
            for dresses in dress_store:
                print("The best dress for you today is ", dress_store[1])
                break
        if ask_question & ask_question2 & ask_question3 == 3 & 3 & 3:
            for dresses in dress_store:
                print("The best dress for you today is ", dress_store[3],".", "Dont drink too much!")
        else:
            print("what you are requesting is not available at the moment")
            Run = False
    except:
        print("Sorry we cant process this command right now, we are still working on this project")