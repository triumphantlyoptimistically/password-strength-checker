running = True
while running:
    password = input("Enter password: ")
    validChoice = False
    while validChoice == False:
        checkAgain = input("Do you want to check another password? Y\\N ")
        if checkAgain == "N":
            validChoice = True
            running = False
        elif checkAgain == "Y":
            validChoice = True
        else:
            print("Please enter Y\\N")
            validChoice = False