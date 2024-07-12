class tringle:
    def __init__(self, a, b, c):
        import math

        if (a+b)>c and (a+c)>b and (b+c)>a:
            s = (a+b+c)/2
            area = math.sqrt(s*(s-a)*(s-b)*(s-c))
            print("Area is:", area)

        else:
            print("not a triangle")

a = float(input("enter the first a: "))
b = float(input("enter the second b: "))
c = float(input("enter the second b: "))

total = tringle(a,b,c)