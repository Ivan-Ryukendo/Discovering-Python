try:
    a = int(input("Enter the value of a: "))
    b = int(input("Enter the value of b: "))
    
    result = a / b
    print(result)
except (ValueError, ZeroDivisionError):
    print("Your input is not correct.")
finally:
    print("Try Again.")