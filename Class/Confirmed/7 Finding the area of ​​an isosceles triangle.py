import math
a = int(input("Enther the value of a: "))
b = int(input ("Enter the Value Of b: "))  #This is for taking inputs from user.
c = int(input ("Enter the Value Of c: "))

if((a+b)>c and (b+c)>a and (c+a)>b):
    S = (a + b + c)/2
    Area = math.sqrt(S*(S-a)*(S-b)*(S-c))

    print(Area)

else:
    print("Tringle is not possible")