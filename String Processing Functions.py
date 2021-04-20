## @author Mya Yazbek
## I pledge my word of honor that I have abided
## by the CSN Academic Integrity Policy while completing
## this assignment.
## @file MyaYazbekcit137_hw5B.py
## @version 2021-04-20
## @brief this program has 5 different functions, which are
## all explained below. It does not use global variables.
## @note This program took me 3 hours to develop, write, test, and debug


##menu function
##offers user a choice of which funciton they would like to run
##@return: registers the user input though and gives it to the
##execution function, no output unless an error message
##@param: user option as input

def menu():
    print("Enter 1 to check the user name")
    print("Enter 2 to check the password")
    print("Enter 3 to find the number of specified characters in a string")
    print("Enter 4 to process various strings")
    print("Enter 5 to exit")

    choice = int(input())
    return choice


##checkName function
##Has the user enter a name to process, checks to see if the name
##entered is 5 characters in length. If true, the name is valid.
##If false, the name is invalid. 
##@return: whether the name is valid or not
##@param: user enters a name to process

def checkName(name):
    if len(name) == 5 and name.isalpha():
        print("user name is valid")
    else:
        print("user name is not valid")

##checkPwd function
##Has the user enter a password to process, checks to see if the
##string entered matches "abc", and is not case sensitive
##@return: whether the password is correct or not
##@param: user enters a password

def checkPwd(pwd):
    if pwd.casefold() == "abc":
        print("password is correct")
    else:
        print("password is incorrect")

##count function
##Has the user enter a string to process, and asks for a specific
##character to search the string for. 
##@return: returns how many times the character is found in the string
##@param: user enters a string and a character to search for


def count(s,c):
    count = s.count(c)
    print(c, "is found", count, "times in this string.")


##processString function
##Has the user enter a string to process
##@return: returns info about the string such as:
##length, upper case, swapped case, first character,
##last character, each character printed on a new line
##and will replace the letter e with the character $
##@param: user enters a string 


def processString(string):

    print("The length of this string is:", len(string))
    print("Upper CASE:", str.upper(string))
    print("Swapped!:", str.swapcase(string))
    print("First character:", string[0])
    print("Last character:", string[-1])
    for ix in range(len(string)):
        print(string[ix], end = "\n")

    print("Replaced string:", string.replace("e","$"))

##execution function
##Has the user enter a string to process
##@return: tells the program which function to run from the user choice
##given by the menu()
##@param: depending on choice user inputs various strings which
##are processed by their corresponding functions
    
def execution():
    choice = menu()
    while choice != 5: #loops the menu()
    
        if choice == 1:
            name = input("Enter a user name to process")
            checkName(name)
            
        elif choice == 2:
            pwd = input("Enter your password")
            checkPwd(pwd)
           

        elif choice == 3:
            s = input("Enter any string you'd like:")
            c = input("Enter a character to search the string for:")
            count(s,c)
          

        elif choice == 4:
            string = input("Enter any string of your choice:")
            processString(string)
         
        else:
            print("Invalid choice, please try again.") #error message
        choice = menu()


execution()


#it works yee haw
#end of assigment 5B
