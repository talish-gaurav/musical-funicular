import random

number = random.randint(1,100)

while True:
    n=int(input("Enter any number between 1-100 (inclusive)"))

    if n>number :
        print("Too high")
    elif n<number :
        print("Too low")
    else:
        print("You got it right")
        break