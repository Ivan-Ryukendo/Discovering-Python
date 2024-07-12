num = int(input("Enther the value of number: "))
if num>1:
    for i in range (2, num):
        if num % i == 0:
            print("Not Prime number")
            break
    else:
        print("Prime number")
else:
    print("Not Prime number")

    
