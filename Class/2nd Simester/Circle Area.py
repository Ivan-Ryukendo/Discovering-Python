import math
def area(r):
    myarea = math.pi*r**2
    return myarea
r = area(int(input("Enter the value of radius: ")))
print("The area of the circle is: ",r)