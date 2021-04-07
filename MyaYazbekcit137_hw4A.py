## @author Mya Yazbek
## I pledge my word of honor that I have abided
## by the CSN Academic Integrity Policy while completing
## this assignment.
## @file MyaYazbekcit137_hw4A.py
## @version 2021-03-23
## @brief this program has 4 different functions, which are
## all explained below
## @note This program took me 13 hours to develop, write, test, and debug


### function 1
##This function accepts as parameters, a list of test scores.
##Make sure to use a Python
##list. The list is passed to this function from the main function.
##@return: total of the values in the list, lowest value,
##highest value, and average of all numbers
##@param: number of test scores
##@param: list of test scores

def test_score_function():
            number_of_test_scores = float(input("Please enter the number of students: ")) #gets the number of scores from the user
            while number_of_test_scores < 1:
                print("Invalid entry, please try again.") 
                number_of_test_scores = float(input("Enter the number of students: "))


            test_scores = [] #creates the list
            while len(test_scores) < number_of_test_scores:
                test_scores.append(float(input("Please enter a test score to add to the list: "))) #adds scores to list
     
##            print("Here is the list of test scores you have entered: ", test_scores)          this line is to check that the list updated
##            print("The length of this list is: ", len(test_scores))                           this line is to check the length of the list
                
            print("The max value of all test scores is: ", format(max(test_scores), ".2f"))
            print("The minimm value of all test scores is: ", format(min(test_scores), ".2f"))

            #finding the average, and the total of the test scores
            
            test_average = 0
            for i in range(len(test_scores)):
                    test_average += (test_scores[i] / number_of_test_scores) #calculates average
            print("The average of all test scores is: ", format(test_average, ".2f"))
            for i in range(len(test_scores)):
                total = sum(test_scores) #calculates sum
            print("The total of all test scores is: ", format(total, ".2f"))

##function 2
##This function accepts as parameters, 2 whole numbers
##and displays all the even numbers between the 2 numbers.
##For example, if the values of the parameters are 10 and 20, the
##function displays all the even numbers between the 2 parameter values.
##@param: two intergers
##@return: list of even numbers between the two values, or -100 if
##second value is less than the first

def even_number_return():
            user_input_1 = int(input("Please enter the first number: ")) #prompts the user for the first number
            user_input_2 = int(input("Please enter the second number: ")) #prompts user for second number
            if user_input_1 > user_input_2:
                print(-100)
            else:
                for i in range(user_input_1,user_input_2+1):
                    if i % 2 == 0: #using the modulo operator to tell the program we only want the even numbers
                        print(i)

##Function 3: This function accepts the number of products to be
##entered by the user as its
##parameter. Inside the function:
##Ask for the price of each item and store the data in a list
##Display the header “Purchase Price Values”
##@param number of products
##@param prices of products
##@return contents of list, length of list, average of prices,
##prompt for user to enter a price,
##and then if the price is found in the list


def purchase_price_values():
                print("Purchase Price Values")
                number_of_products = float(input("Please enter the number of products: ")) #asks user for the number of items
                
                while number_of_products < 1:
                        print("Invalid entry. Please try again.\n")
                        number_of_products = float(input("Please enter the number of products: ")) #checks to make sure the number entered is more than 1
                        
                prices = [] #creates the list of prices
                while len(prices) < number_of_products:
                        prices.append(float(input("Please enter the prices of the product: ")))
                        product_total = sum(prices)

                # gives us an output of simple data 
                print("The list of prices you have entered is: ", prices)
                print("The length of this list is: ", len(prices))
                print("The total of all products is:", format(product_total, ".2f"))
                print("The average price of all products is:", format((product_total / number_of_products), ".2f"))

                #a simple index to have the program search the list for a specific price

                found = 0
                while found == 0:
                        search_price = float(input("Enter a price value to search for: "))
                        if search_price in prices:
                                print("Item price found!")
                                found = 1
                        else:
                            print("No products match this price.")
                            found = 0


#function 0
#provide a series of options and allows the user
#to chose which function to run
#@return: the user choice.
#@param: none


def main_function():
        user_request = int(input("\nEnter 1 to process test scores\nEnter 2 to process even numbers \nEnter 3 to process purchase prices \nEnter 4 to exit"))
        while user_request > 4 or user_request < 1:
            print("\nPlease enter a number between 1 - 4 to use this program.")
            user_request = int(input("\nEnter 1 to process test scores\nEnter 2 to process even numbers \nEnter 3 to process purchase prices \nEnter 4 to exit"))
        while user_request != 4:
                if user_request == 1:
                    test_score_function() #processes test scores
                    main_function() #returns us to the start menu
                elif user_request == 2:
                    even_number_return() #even number function
                    main_function() #returns us to the start menu
                elif user_request == 3:
                    purchase_price_values() #purchase price values function
                    main_function() #returns us to the start menu
        if user_request == 4:
                print("Thank you for using the program. Goodbye!")
                quit()

#below calls the main function which will then execute the rest

main_function()

#it works! yeehaw
#end of assigment 4A













