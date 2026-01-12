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

def Check_Lowercase(password):
    for i in range(len(password)):
        if password[i - 1].islower():
            return True
        else:
            continue
    return False

def Check_Number(password):
    for i in range(len(password)):
        if password[i - 1].isnumeric():
            return True
        else:
            continue
    return False

def Check_Special_Char(password):
    specialChars = ['!','@','\#','$','%','^','&','*','(',')','_','+','-','=','?','/','.']
    for i in range(len(password)):
        if password[i] in specialChars:
            return True
        else:
            continue
    return False

def Calculate_Strength(score):
    if score < 2:
        return "Weak"
    elif score < 4:
        return "Medium"
    else:
        return "Strong"


running = True

while running:

    rulesFailed = []
    password = input("Enter password: ")
    score = 0

    if Check_Length(password) == True:
        score = score + 1
    else:
        rulesFailed.append("Ensure your password is at least 8 characters long")

    if Check_Uppercase(password) == True:
        score = score + 1
    else:
        rulesFailed.append("Use an uppercase character")

    if Check_Lowercase(password) == True:
        score = score + 1
    else:
        rulesFailed.append("Use a lowercase character")

    if Check_Number(password) == True:
        score = score + 1
    else:
        rulesFailed.append("Use a number")

    if Check_Special_Char(password) == True:
        score = score + 1
    else:
        rulesFailed.append("Use a special character")

    print(f"Password strength: {Calculate_Strength(score)}")
    if len(rulesFailed) > 0:
        print("To improve your password:")
        for i in range(len(rulesFailed)):
            print(rulesFailed[i])

    running = Go_Again()   