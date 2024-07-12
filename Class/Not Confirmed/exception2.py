try:
    a = int(input("Enter the value of a: "))
    b = int(input("Enter the value of b: "))
    
    result = a / b
    print(result)
except ZeroDivisionError:
    print("Your input is not correct.")
finally:
    print("We are expensive lazy.")