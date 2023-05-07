import secrets

all = ""
password = ""

upperCaseLetters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowerCaseLetters = upperCaseLetters.lower()
digits = "1234567890"
symbols = "~!@#$%^&*()-_+={}[]\\|;:'\",./?"
while (True):
    upper = input("Do you want to include upper case letters? Type Y or N. ").upper()
    if (upper == "Y"):
        all += upperCaseLetters
        break
    elif(upper == "N"):
        break
    else:
        print("Invalid Input")

while (True):
    lower = input("Do you want to include lower case letters? Type Y or N. ").upper()
    if (lower == "Y"):
        all += lowerCaseLetters
        break
    elif(lower == "N"):
        break
    else:
        print("Invalid Input")

while (True):
    digs = input("Do you want to include digits? Type Y or N. ").upper()
    if (digs == "Y"):
        all += digits
        break
    elif(digs == "N"):
        break
    else:
        print("Invalid Input")

while (True):
    syms = input("Do you want to include symbols? Type Y or N. ").upper()
    if (syms == "Y"):
        all += symbols
        break
    elif(upper == "N"):        
        break
    else:
        print("Invalid Input")

while (True):
    lengthOfPassword = input("Type password length: ")
    try:
        lengthOfPassword = int(lengthOfPassword)
        break
    except:
        print("Invalid Input")

while (True):
    remove = input("Are there any upper case letters, lower case letters, digits, or symbols that are not accepted? Y or N.  ")
    if (remove == "Y"):
        letter = input("Type the upper case letter, lower case letter, digit, or symbol: ")
        try:
            all.remove(letter)
        except:
            print("Invalid Input")
    elif(remove == "N"):
        break
    else:
        print("Invalid Input")

for i in range(lengthOfPassword):
    password += secrets.choice(all)

print("Password: " + password)

