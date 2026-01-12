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

running = True
while running:
    rulesFailed = []
    password = input("Enter password: ")
    score = 0
    if Check_Length(password) == True:
        score = score + 1
    else:
        rulesFailed.append("Length rule")
    running = Go_Again()