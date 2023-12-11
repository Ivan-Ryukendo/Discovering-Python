n = int(input("Enther the value of n: "))

if n > 100:
    print("This is notcorrect.") # Your Valuse can't be more then 100.
elif n>= 80:
    print("You Got A+") # 40 - 49
elif n>= 70:
    print("You Got A") # 40 - 49
elif n>= 60:
    print("You Got A-") # 60 - 69
elif n>= 50:
    print("You Got B+") # 50 - 59
elif n>= 40:
    print("You Got B") # 40 - 49
elif n>= 30:
    print("You Got B-") # 30 - 39
else:
    print("You failed") # Less then 30. Then Fialed.