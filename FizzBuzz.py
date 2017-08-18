

def fizz_buzz(fizz, buzz, end):

    index = 1

    while index <= end:
        if index % fizz == 0 and index % buzz == 0:
            print("FizzBuzz")
        elif index % fizz == 0:
            print("Fizz")
        elif index % buzz == 0:
            print("Buzz")
        else:
            print(index)

        index += 1

fizz_buzz(3, 7, 100)
