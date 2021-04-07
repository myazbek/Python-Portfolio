## @author Mya Yazbek
## I pledge my word of honor that I have abided
## by the CSN Academic Integrity Policy while completing
## this assignment.
## @file MyaYazbek137_pa3A.py
## @version 2021-02-06
## @brief This assignment contains 2 parts.
## The first section consists of a program that 
## prompts the user for their name, and a number between 1 - 10
## and outputs the roman numeral associated with that integer.
## an error message will occur if the number is not between 1 - 10
## The second program that asks the user to input the year, month and
## number date to calculate the day of the week using Ziller's rule
## error messages will occur if the day of the month/year is too big or small
## @note This code took me 5 hours to develop, write, test, and debug
## My biggest issue was a simple syntax error that took 2 hours to
## find and fix lol

#start of part 1, roman numeral program
#here I will ask the user for their name

print("Please enter your name.")
name = input()

#here I will print their name and ask the user to
#input a number between 1 - 10

print("Hello, ", name, "! Please enter a whole number between 1 - 10.", sep="")
number = int(input())

#This is the part of the code that will output an error message if a number
#less that 1 or greater than 10 is entered. It will
#prompt the user to try again.

if number > 10:
    print("Error. This number is over 10. Please try again.")
    
if number < 1:
    print("Error. This number is less than 1. Please try again.")

#now comes the part where we convert the input to roman numeral
#using the if/else/elif funcitons

if number == 1:
    print(name, ", your roman numeral is I.")
else:
    if number == 2:
        print(name, ", your roman numeral is II.")
    elif number == 3:
        print(name, ", your roman numeral is III.")
    elif number == 4:
        print(name, ", your roman numeral is IV.")
    elif number == 5:
        print(name, ", your roman numeral is V.")
    elif number == 6:
        print(name, ", your roman numeral is VI.")
    elif number == 7:
        print(name, ", your roman numeral is VII.")
    elif number == 8:
        print(name, ", your roman numeral is VIII.")
    elif number == 9:
        print(name, ", your roman numeral is IX.")
    elif number == 10:
        print(name, ", your roman numeral is X.")

#end of program 1


#beginning of program 2
#ziller's rule
# H = (q + 26 (m+1) /10 + k + k/4 + j/4 + 5j) % 7


#first ask the user in input a year, month number, and day of month,
#in this order.
#i'm going to add the error messages to this as well 

print("Hello! Please input the year")
year = int(input())
if year <= 1 or year >= 2022:
    print("Invalid year entry. Please try again.")
    
#now we will ask the user to input the month
#we need to accomodate the formula adjustments for january and february
#by using two if statements, found underneath the month_number error lines

print("Now please enter the month number.")
month_number = int(input())
if month_number < 1 or month_number > 12:
    print("Invalid month number. Please try again and enter a number between 1 - 12.")
if month_number == 1:
    month_number = month_number + 12
    year = year - 1
if month_number == 2:
    month_number = month_number + 12
    year = year - 1

#lastly, we will receive the day of month from the user

print("Lastly, please enter the number date of the month.")
day_of_month = int(input())
if day_of_month < 1 or day_of_month > 31:
          print("Invalid day of month. Please enter a number between 1 - 31.")

print("Thanks! I am now computing the day of the week.")

#lets set the rest of the variables needed for the formula
#like year_of_century and century

century = year // 100

year_of_century = year % 100

#okay so using the handy dandy key for this formula in the assignment
#document, I will now tell Python how to take the information above
#and spit out the day of the week.
#we will make sure to use interger division for this,
#as the formula won't work otherwise

calculated_day_of_week = ((day_of_month + 26 * (month_number + 1) // 10) + year_of_century + (year_of_century // 4) + (century // 4) + (century * 5)) % 7

#lastly, I will assign the week day to their respective number
#and tell python to spit out the day of the week

print()
if calculated_day_of_week == 0:
    print("The day of the week is Saturday")
else:
    if calculated_day_of_week == 1:
        print("The day of the week is Sunday")
    elif calculated_day_of_week == 2:
        print("The day of the week is Monday")
    elif calculated_day_of_week == 3:
        print("The day of the week is Tuesday")
    elif calculated_day_of_week == 4:
        print("The day of the week is Wednesday")
    elif calculated_day_of_week == 5:
        print("The day of the week is Thursday")
    elif calculated_day_of_week == 6:
        print("The day of the week is Friday")

#it works, can i get a yeehaw in the chat please
#end of assignment 3


