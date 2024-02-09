#!/usr/bin/env python3

def main():

    # a dictionary of the month and stone color values
    stones = {"January": "Garnet", "February": "Amethyst", "March": "Aquamarine", "April": "Diamond", "May": "Emerald", "June": "Alexandrite", "July": "Ruby", "August": "Peridot", "September": "Sapphire", "October": "Tourmaline", "November": "Topaz", "December": "Blue Topaz"}

    #TODO minimize all input to make program more rubust 
    # welcome the user
    print("Welcome to the birthstone generator!")
    # loop to prompt the user
    while True:
        # get user input 
        user_input = input("Would you like to know your Birthstone? Yes/No ")
        # ask for the month and print out the responce
        #TODO add reponse for a not valid input/month
        if user_input == "Yes":
            month = input("In what month were you born? ")
            print(f"Your birthstone for the month of {month} is {stones.get(month)}")
            break
        # exit the loop
        elif user_input == "No":
            print("Goodbye")
            break
        # account for iput other than yes or no
        else:
            print("Input not valid please try again")
            

if __name__ == "__main__":
    main()

