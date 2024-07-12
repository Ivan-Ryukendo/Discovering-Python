class bignumber:
    def __init__(self, a, b, c):
        if (a > b) and (a > c):
            print("A is Large Number")
        elif (b > c) and (b > c):
            print("B is Large Number")
        else:
            print("C is Large Number")

a = int(input("Enter the Value of A: "))
b = int(input("Enter the Value of B: "))
c = int(input("Enter the Value of C: "))

large = bignumber(a,b,c)