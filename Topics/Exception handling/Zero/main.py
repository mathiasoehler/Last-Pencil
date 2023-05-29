n = int(input())
denominator = int(input())

try:
    a = n // denominator
except ZeroDivisionError:
    print("Division by zero is not supported")
except ValueError:
    print("")
else:
    print(n // denominator)
