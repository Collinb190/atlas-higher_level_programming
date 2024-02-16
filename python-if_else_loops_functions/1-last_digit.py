#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
n = "-" if number < 0 else ""
lNum = abs(number) % 10
if lNum > 5 and number > 0:
    print(f"Last digit of {number} is {n}{lNum} and is greater than 5")
elif lNum == 0:
    print(f"Last digit of {number} is {n}{lNum} and is 0")
elif lNum < 6 or number < 0:
    print(f"Last digit of {number} is {n}{lNum} and is less than 6 and not 0")
