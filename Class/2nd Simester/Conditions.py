def Conditions():
    
    a = int(input("Input the value of a: "))
    b = int(input("Input the value of b: "))
    c = int(input("Input the value of c: "))

    if ((a>b)and(a>c)):
        print("The greatest number is A as", a)
    elif ((b>a)and(b>c)):
        print("The greatest number is B as", b)
    else:
        print ("The greatest number is C as", c)

Conditions()