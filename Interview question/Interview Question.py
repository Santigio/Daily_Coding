List1 = [1, 2, 2, 3, 3]


#for specific element
def sigle_duplicate():
    List2 = [i for i in range(len(List1))
    if List1[i] == 3]
    return List2


#For any element
def all_duplicate():
    global a
    y = []
    for a in List1:
        if not a in y:
            y.append(List1)
        print(a)



list3 = ["We are here to stay", "Bob is a great man", "You are getting better at programming", "Love you"]


def spam_detection():
    for i in list3:
        if "Love you" in i:
            print("1 Error found in line ", len(list3), "=", i)


spam_detection()

