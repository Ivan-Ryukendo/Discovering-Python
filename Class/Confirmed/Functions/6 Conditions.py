def Conditions():
    
    a = int(input("Input the "))
    b = 318
    c = 653
    d = 446
    e = 800

    if ((a>b)and(a>c)and(a>d)and(a>e)):
        print("The greatest number is", a, "!")
    elif ((b>a)and(b>c)and(b>d)and(b>e)):
        print("The greatest number is", b,"!")
    elif ((c>a)and(c>b)and(c>d)and(c>e)):
        print("The greatest number is", c,"!")
    elif ((d>a)and(d>b)and(d>c)and(d>e)):
        print("The greatest number is", d,"!")
    else:
        print ("The greatest number is", e ,"!")

Conditions()