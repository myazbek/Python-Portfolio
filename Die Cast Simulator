##die simulator

print("Welcome to my very hot and very cool die cast simulator!\n")

def die_caster():
    print("\nSelect which type of die you should like to cast.")
    die_selection = input("Enter 4 for d4, 6 for d6, 8 for d8, 10 for d10, 00 for d00 (percentile),\n12 for d12, or 20 for d20. Enter DONE when done: ")

    import random, math

    while die_selection != ("DONE"):
        if die_selection == ("4"):
            print(random.randint(1, 4))
            die_caster()
        elif die_selection == ("6"):
            print(random.randint(1, 6))
            die_caster()
        elif die_selection == ("8"):
            print(random.randint(1, 8))
            die_caster()
        elif die_selection == ("10"):
            print(random.randint(1, 10))
            die_caster()
        elif die_selection == ("00"):
            print(random.randint(1, 100))
            die_caster()
        elif die_selection == ("12"):
            print(random.randint(1, 12))
            die_caster()
        elif die_selection == ("20"):
            print(random.randint(1, 20))
            die_caster()
        else:
            print("Invalid entry. Please try again.")
            die_caster()
        
    if die_selection == ("DONE"):
        print("Thanks for using my very hot and very cool die cast simulator. Goodbye!")
        quit()


die_caster()
