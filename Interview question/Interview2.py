def remove_even():
    arr = [1, 2, 3, 4, 5, 6, 7, 8]
    for i in arr:
        if i % 2 == 0:
            arr.remove(i)
    print(arr)


remove_even()
