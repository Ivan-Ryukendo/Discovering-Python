def factorial(num):
    if num ==0 or num ==1:
        return 1
    else:
        return num * factorial(num-1)
num=5
print(num, "factorial is", factorial(num))