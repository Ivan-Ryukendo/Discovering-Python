#Enter input
n = int(input("Enter input number : "))
 
fact = 1

if n == 0 or n == 1:
    print("The factorial is 1")
else:
    for i in range(1, n + 1):
        fact = fact * i
    print("The factorial of",n,"is",fact)
