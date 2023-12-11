def leepyear():

    year = int(input("Enter the year: "))

    if (year % 400 == 0) and ((year % 4 == 0) or (year % 100 != 0)):
        print("Leap Year")
    else:
        print("Noe Leep Year")

leepyear()