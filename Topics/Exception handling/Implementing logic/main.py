try:
    name, surname = input().split()
    print("Welcome to our party,", name, surname)
except ValueError:
    print("You need to enter exactly 2 words. Try again!")
from m