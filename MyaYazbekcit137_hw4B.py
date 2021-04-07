## @author Mya Yazbek
## I pledge my word of honor that I have abided
## by the CSN Academic Integrity Policy while completing
## this assignment.
## @file MyaYazbekcit137_hw4B.py
## @version 2021-04-06
## @brief this program has 4 different functions, which are
## all explained below. It does not use global variables.
## @note This program took me 10 hours to develop, write, test, and debug


##menu function
##offers user a choice of which funciton they would like to run
##@return: nothing, registers the user input though
##@param: user option as input

def menu():

    #printing all our options, storing user choice
    
    print("Welcome to my Program!")
    print("Enter 1 to process course data")
    print("Enter 2 to process state capitals")
    print("Enter 3 to process IP addresses")
    print("Enter 4 to exit")
    user_option = int(input("Please enter your selection here:"))
    return user_option


### function 1
##This function accepts course number and outputs the course title,
##meeting day, and instructor. It uses a dictionary in the function.
##@return: course title, meeting day, instructor
##@param: course number

def course_data():
    course = input("\nWelcome to the Couse Data Processing Function!\nEnter DONE when finished\nPlease enter a course number to process: ")

    #our dictionaries are below this line for course title, instructor, and meeting day
    course_title = {"CIT137" : "Python Programming", "IS115" : "Introducion to Programming", "CS135" : "Computer Science I"}
    course_instructor = {"CIT137" : "Alan Turing", "IS115" : "Carol Shaw", "CS135" : "Ada Lovelace"}
    meeting_day = {"CIT137" : "Monday", "IS115" : "Tuesday", "CS135" : "Friday"}

    #loop for our course search
    while course != ("DONE"):
        if course in course_title:
            print("\nThe title of", course, "is", course_title[course])
            print("This course is taught by", course_instructor[course])
            print("This course meets on", meeting_day[course])
            course = input("\nWelcome to the Couse Data Processing Function!\nEnter DONE when finished\nPlease enter a course number to process: ")
        if course != ("DONE") and course not in course_title:
            print("Sorry, the course number you have entered is not in our database. Please try again.")
            course = input("\nWelcome to the Couse Data Processing Function!\nEnter DONE when finished\nPlease enter a course number to process: ")

    #sentinel value to end this function
        if course == ("DONE"):
            print("Thank you for using this program. Have a nice day!")
            

### function 2
##This function accepts a state and outputs
##the state's capital city. It uses a dictionary in the function.
##@return: Capital city
##@param: state

def state_capitals():
    
    #defining our dictionary
    #i didn't realize we only needed a few states, I put all of them in my dictionary ;-;
    
    states_and_capitals = {"Alabama" : "Montgomery", "Alaska" : "Juneau", "Arizona" : "Pheonix", "Arkansas" : "Little Rock", "California" : "Sacramento", "Colorado" : "Denver", "Connecticut" : "Hartford", "Delaware" : "Dover", "Florida" : "Tallahassee", "Georgia" : "Atlanta", "Hawaii" : "Honolulu", "Idaho" : "Boise", "Illinois" : "Springfield", "Indiana" : "Indianapolis", "Iowa" : "Des Moines", "Kansas" : "Topeka", "Kentucky" : "Frankfort", "Louisiana" : "Baton Rouge", "Maine" : "Augusta", "Maryland" : "Annapolis", "Massachusetts" : "Boston", "Michigan" : "Lansing", "Minnesota" : "Saint Paul", "Mississippi" : "Jackson", "Missouri" : "Jefferson City", "Montana" : "Helena", "Nebraska" : "Lincoln", "Nevada" : "Carson City", "New Hampshire" : "Concord", "New Jersey" : "Trenton", "New Mexico" : "Santa Fe", "New York" : "Albany", "North Carolina" : "Raleigh", "North Dakota" : "Bismarck", "Ohio" : "Columbus", "Oklahoma" : "Oklahoma City", "Oregon" : "Salem", "Pennsylvania" : "Harrisburg", "Rhode Island" : "Providence", "South Carolina" : "Columbia", "South Dakota" : "Pierre", "Tennessee" : "Nashville", "Texas" : "Austin", "Utah" : "Salt Lake City", "Vermont" : "Montpelier", "Virginia" : "Richmond", "Washington" : "Olympia", "West Virginia" : "Charleston", "Wisconsin" : "Madison", "Wyoming" : "Cheyenne"}
    state_search = input("\nEnter a state to find the corresponding capital city.\nEnter DONE to return to the main menu. \nState search: ")

    #the state search loop, which will allow the user to enter any number of states to search for
    #the sentinel value DONE will end the loop

    while state_search != ("DONE"):
        if state_search in states_and_capitals:
            print("The capital of", state_search, "is", states_and_capitals[state_search])
            state_search = input("\nEnter a state to find the corresponding capital city.\nEnter DONE to return to the main menu. \nState search: ")
        elif state_search not in states_and_capitals:
            print("Sorry, the state you have entered is not in the dictionary. Please try again")
            state_search = input("\nEnter a state to find the corresponding capital city.\nEnter DONE to return to the main menu. \nState search: ")

    #sentinel value to end this function
    if state_search == ("DONE"):
        print("Thank you for using this program. Have a nice day!")


### function 3
##This function accepts an IP address and outputs
##the end of the address and a total count
##it will also return the complete list of IP addresses in the dictionary
##@return: End IP, total count, complete dictionary
##@param: beginning IP address

def ip_addresses():
    ip_dictionary = {"1.0.0.0" : ("1.0.0.255", "256"),"1.1.1.0" :("1.1.1.0","1"), "1.1.1.2" : ("1.1.1.255", "254")}

    #asking the user for the beginning of the IP address they would like to search
    ip_search = input("Enter the beginning of the IP address you would like to search.\nEnter DONE when done.")
    while ip_search != ("DONE"):
        
        print(ip_dictionary) #prints the full dictionary


        if ip_search in ip_dictionary: #finds if the input was in the dictionary, gives us our output
            print("End IP address and total count =", ip_dictionary[ip_search])
            ip_search = input("Enter the beginning of the IP address you would like to search.\nEnter DONE when done.")

        #error message if ip_search is not in the dictionary
        if ip_search not in ip_dictionary and ip_search != ("DONE"):
            print("Sorry, this is not a valid IP address. Please try again.")
            ip_search = input("Enter the beginning of the IP address you would like to search.\nEnter DONE when done.")
            if ip_search == ("DONE"):
                    print("Thank you for using this program. Have a nice day!")
        
    #our sentinel value to end the loop
    if ip_search == ("DONE"):
        print("Thank you for using this program. Have a nice day!")

#menu options 

def execution():
    user_option = int(input("\nMain Menu\n Enter 1 to process course data\n Enter 2 to process state capitals\n Enter 3 to process IP addresses\n Enter 4 to exit"))
    while user_option > 4 or user_option < 1:
            print("\nPlease enter a number between 1 - 4 to use this program.")
            user_option = int(input("\nEnter 1 to process test scores\nEnter 2 to process even numbers \nEnter 3 to process purchase prices \nEnter 4 to exit"))


    while user_option != 4:
            if user_option == 1:
                    course_data()
                    execution() #returns us to the start menu after the functions runs all the way through
            elif user_option == 2:
                    state_capitals() 
                    execution() 
            elif user_option == 3:
                    ip_addresses()
                    execution() 
    if user_option == 4:
                print("Thank you for using the program. Goodbye!")
                quit()

#calling the main menu, which will execute the user option for whichever
#above program they want to use

execution()
