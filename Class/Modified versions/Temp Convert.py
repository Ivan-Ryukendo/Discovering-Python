while True:
    choice  = input("What do you want to convert into?\nPick the conversion mathord\n 1. Fahrenheit to Celsius\n 2. Celsius to Fahrenheit\n 3. Exit\n")

    if choice == "1":

        F = int(input("Enter the value in Fahrenheit: "))
    
        C = ((F - 32) * 5) / 9
    
        print("Your Celsius will be:", C)

    elif choice == "2":
        C = int(input("Enter the value of Celsius: "))

        F = (C*9/5)+32

        print("Your Fahrenheit will be:", F)
    
    elif choice == "3":
        break

    else:
        print("Please pick what do you want to do 1, 2, or 3.")

        user_choice = input("You don't want to convert? (yes/no): ")
    
        if user_choice != "yes":
            break
