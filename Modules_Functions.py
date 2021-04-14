## @author Mya Yazbek

## @brief this program has 4 different functions, which are
## all explained below. It does not use global variables.
## running this program will not produce any output.
## it requires an executor function, which is located in
## another file named: Modules_Functions_executor



##menu function
##offers user a choice of which funciton they would like to run
##@return: registers the user input though and gives it to the
##execution function, no output unless an error message
##@param: user option as input

def menu():
    print("Enter 1 to perform math operations")
    print("Enter 2 to simulate die being thrown")
    print("Enter 3 to show system information")
    print("Enter 4 to exit")
    choice = int(input())

    if choice < 1 or choice > 4:  #error message
        print("Invalid entry. Please try again.")
        choice = int(input())

    return choice

##math function
##offers user a choice of which funciton they would like to run
##@return: PI, SINE of num, COSINE of num, TANGENT of num,
##NAT LOG of num, smallest int >= num, largest int <= num
##@param: user enters a number to process

def math_function(num):
    import math

    print("PI =", format(math.pi, ".4f"))
    print("SINE =", format(math.sin(math.radians(num)), ".4f"))
    print("COSINE =", format(math.cos(math.radians(num)), ".4f"))
    print("TANGENT =", format(math.tan(math.radians(num)), ".4f"))

    if num == 0:
        print("Error: Cannot take the natural log of 0")
    else:
        print("NATUAL LOG =", format(math.log(num), ".4f"))
        
    print("The smallest interger greater than or equal to", num, "is:", format(math.ceil(num), ".4f"))
    print("The largest interger smaller than or equal to", num, "is:", format(math.floor(num), ".4f"))


##die simulator function
##simulates the throwing of a 6 sided die as many times
##as the user wants. It will also ask the user for
##a value to check, and will tell us how many times that value
##is thrown
##@return: list of die cast, how many times a specified value
##appears in the list of die casts. 
##@param: number of times the die will be thrown, a value to check

def die_simulator(number_of_throws, value_check):
    import math, random
    
    die_list = [] #an empty list to be appended by randint
    for x in range(number_of_throws):
        die_list.append(random.randint(1, 6))

    
    num_value = die_list.count(value_check)

    print("\nDice Report")

    for n in die_list: #formatting the way the hw wants the output to look
        print(n)
    
    print("The number of times", value_check, "was thrown is:", num_value)


##system info funciton
##tells the user various things about their computer
##@return: platform machine, processor, system, python version data
##OS version 
##@param: nothing

def system_info():
    import platform

    print("Underlying layers:", platform.platform())
    print("Machine:", platform.machine())
    print("Processor:", platform.processor())
    print("System:", platform.system())
    versionData = platform.python_version_tuple()
    print("Python implementation:", platform.python_implementation())
    print("Python version data:", platform.python_version())
    print("Python version:", versionData[0])
    print("Python version:", versionData[1])
    print("Python version:", versionData[2])
    print("OS version:", platform.version())





##below is the executor function that can be found in the executor file
##def executor():
##    choice = menu()
##    if choice == 1:
##        num = float(input("Please enter a number to process: "))
##        math_function(num)
##        menu()
##    elif choice == 2:
##        number_of_throws = int(input("Enter the number of times to throw the dice:"))
##        value_check = int(input("Enter a value to check:"))
##        die_simulator(number_of_throws, value_check)
##        menu()
##    elif choice == 3:
##        system_info()
##        menu()
##
##executor()


