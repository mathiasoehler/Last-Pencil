a = int(input())
b = int(input())

try:
    c = a / b
    print(c)

except ZeroDivisionError:
    print("The Error!")
