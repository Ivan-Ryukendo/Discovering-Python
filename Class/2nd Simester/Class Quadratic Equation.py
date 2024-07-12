class Quardratic:
    def __init__(self, a, b, c):
        import math
        d = (b*b)-(4*a*c)

        if d == 0:
            x = -b / (2*a)
            print("Root are: ", x)
        elif d > 0:
            x1 = (-b + math.sqrt(d) / (2 * a))
            x2 = (-b - math.sqrt(d) / (2 * a))
            print("Root are: ", x1, x2)
        else:
            print("Root is imaginary")

a = float(input("Enter the value of A: "))
b = float(input("Enter the value of B: "))
c = float(input("Enter the value of C: "))

result = Quardratic(a,b,c)