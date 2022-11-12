#Password generator - created by Avi

import random

print("Welcome to the random password generator. ")

def easyPasswordGenerator():
    #elements of a easy password

    numbers=["1",'2',"3","4","5","6","7","8","9","0"]
    words=["sense","planes","position","circle","vase","nation","fruit","advertisment","cat","harbor","cakes","use","brother","bike","example","playground","lettuce","smile","summer","dress","vest","nest","protest","deer","rail","suit","look","hour","planets","strech","governor","sail","hope","hair","python","coding"]

    easy_password=""

    choice_number_1=random.choice(numbers)
    choice_number_2=random.choice(numbers)
    choice_word_1=random.choice(words)
    choice_word_2=random.choice(words)
    easy_password=choice_word_1+"-"+choice_word_2+"-"+choice_number_2+choice_number_1

    print("Your password is", easy_password)

    print(" 1 - Save the password")
    print (" 2  - Do not save the password")

    ch3=input(" Enter your choice.")
    if ch3=="1":
        file=open("password.txt","w")
        content=file.write(easy_password)
        print(content)
        file.close()

    elif "2":
        print("Password was not saved.")

    else:
        print("invalid input")
def passwordGenerator():
    passwordLenght=int(input("what is the number of charaters in your password: "))

    # elements of password
    specialCharacters=["!","@","#","$","%","^","&","*","?"]
    letters=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    numbers=["1",'2',"3","4","5","6","7","8","9","0"]
    uppercaseLetters=[]

    for i in letters:
        uppercaseLetters.append(i.upper())

    elements=[specialCharacters,numbers,letters,uppercaseLetters]

    password=""

    for i in range(passwordLenght):
        element=random.choice(elements)
        character=random.choice(element)
        password=password+character

    print("Your password is",password)

    print(" 1 - Save the password")
    print (" 2  - Do not save the password")

    ch3=input(" Enter your choice.")
    if ch3=="1":
        file=open("password.txt","w")
        content=file.write(password)
        print(content)
        file.close()

    elif "2":
        print("Password was not saved.")

    else:
        print("invalid input")

while True:
    print("1 - Generate password. Normal mode.")
    print("2 - Generate password. Easy mode.  ")
    print("3 - Exit")
    print('4 - Information')
    ch = input("Enter your choice: ")
    
    if ch=="1":
        passwordGenerator()
    elif ch=="2":
        easyPasswordGenerator()
    elif ch=="3":
        print("Thanks for using the random password generator!")
        break
    elif ch=="4":
        print("1 - Information on normal mode password generator")
        print("2 - Information on easy mode password generator")
        print("3 - Information about creator of the program")
        print("4 -Go back to main menu.")
        ch2=input("Enter your choice: ")
        if ch2=="1":
            print("The normal password generator generators a password that can be however long you want. The password consists of numbers, uppercase letters, lowercase letters, and special characters.")
        if ch2=="2":
            print("The easy password generator generators a password in a format that is much easier to remember. The format for the psasword is 2 random words split by a hyphen and one random 2 digit number also split by a hyphen. A example of this is Python-park-57")
        if ch2=="3":
            print("The creator of this program is Avi Sawhney. Avi is a 11 year old boy who likes sports, computers, and video games. Avi is currently entering 6th grade and hopes to get better at everything he does.")
        if ch2=="4":
            continue

    else:
        print("invalid input")