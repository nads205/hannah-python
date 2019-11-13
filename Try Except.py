


try:
    answer = 10/0
    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError:
    print(err)
except ValueError:
    print("invalid input")