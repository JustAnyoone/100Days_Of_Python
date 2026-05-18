for list in range(1, 101):

    if list % 3 == 0 and list % 5 == 0:
        print("FizzBuzz")
    elif list % 3 == 0 :
        print("Fizz")
    elif list % 5 == 0 :
        print("Buzz")
    else : print(list)