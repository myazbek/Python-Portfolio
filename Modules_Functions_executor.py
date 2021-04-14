## @author Mya Yazbek

## @brief this program contains one function that executes
## three other functions from the file Modules_Functions

from Modules_Functions import menu, math_function, die_simulator, system_info


##execution function
##runs the functions in the above file
##@return: the function chosed by the user
##@param: none, takes the user option from the menu function in the other file


def executor():
    
    choice = menu()
    while choice != 4:
        if choice == 1: #number processor
            num = float(input("Please enter a number to process: "))
            math_function(num)

        elif choice == 2: #die simulator
            number_of_throws = int(input("Enter the number of times to throw the dice:"))
            value_check = int(input("Enter a value to check:"))
            die_simulator(number_of_throws, value_check)
    
        elif choice == 3: #system info
            system_info()

        else:
            print("Invalid entry, please try again.")

        choice = menu() #loops the menu until the sentinel value 4 ends the program


executor()
