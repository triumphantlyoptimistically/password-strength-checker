def Go_Again():
    validChoice = False
    while validChoice == False:
        checkAgain = input("Do you want to check another password? Y\\N ")
        if checkAgain == "N":
            return False
        elif checkAgain == "Y":
            return True
        else:
            print("Please enter Y\\N")
            validChoice = False

def Check_Length(password):
    if len(password) >= 8:
        return True
    else:
        return False

def Check_Uppercase(password):
    for i in range(len(password)):
        if password[i - 1].isupper():
            return True
        else:
            continue
    return False


running = True

while running:

    rulesFailed = []
    password = input("Enter password: ")
    score = 0

    if Check_Length(password) == True:
        score = score + 1
    else:
        rulesFailed.append("Length rule")

    if Check_Uppercase(password) == True:
        score = score + 1
    else:
        rulesFailed.append("Uppercase rule")

    running = Go_Again()