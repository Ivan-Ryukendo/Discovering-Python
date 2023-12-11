while True:
    choice  = input("What do you want to convert into?\nPick the conversion mathord\n 1. Fahrenheit to Celsius\n 2. Celsius to Fahrenheit\n 3. Exit\n")

    if choice == "1":

        F = float(input("Enter the value in Fahrenheit: "))
    
        C = ((F - 32) * 5) / 9

        K = -273.1

        if (C < K):

            print("Thats too cold it can't be processed.\n")

        else:
    
            print("Your Celsius will be:", C)
        

    elif choice == "2":
        C = float(input("Enter the value of Celsius: "))

        F = (C * 9 / 5) + 32

        K = -459.67

        if (F < K):
            print("Thats too cold it can't be processed.\n")

        else:
            print("Your Fahrenheit will be:", F)
    
    elif choice == "3":
        break

    else:
        print("Please pick what do you want to do 1, 2, or 3.")

        user_choice = input("You don't want to convert? (yes/no): ")
    
        if user_choice != "yes":
            break
