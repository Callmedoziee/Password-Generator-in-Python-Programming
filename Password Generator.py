print("Welcome to Password Generator, we'd help you create complex passwords")
query = input("To have characters from your name and other details, type Y for yes, if you just want random characters, type N for no: ")
import random

firstname = ""
lastname = ""
details = []
count = 0
newpassword = ""
Bank = list(range(1,10))
randomBank = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w ', 'x', 'y', 'z'] + Bank



if query == "Y" or query == "y":
    print(" You have selected to form your password from your details!")
    firstname = input("Enter First name: ")
    for i in firstname:
        details.append(i)
    lastname = input("Enter last name: ")
    for j in lastname:
        details.append(j)
    birthYear = input("Enter year of birth: ")
    for y in birthYear:
        details.append(y)
    food = input("What's your favourite food? ")
    for f in food:
        details.append(f)
    charNum = int(input("How many characters do you want your password to be (Not more than 16): "))
    if charNum < 16:
        while count < charNum:
            num = random.randint(0, len(details))
            newpassword += details[num]
            count += 1
        print("Your new password is: ", newpassword)
    else:
        print("16 is the maximum number of characters")

elif query == "N" or query == "n":
    print("You have chosen to get a random password")
    charNum = int(input("How many characters do you want your password to be (Not more than 16): "))
    if charNum < 16:
        while count < charNum:
            num = random.randint(0,len(randomBank)-1)
            newpassword += str(randomBank[num])
            count += 1
        print("Your new password is: ", newpassword)
    else:
        print("16 is the maximum number of characters")
else:
    print("Wrong Input")




