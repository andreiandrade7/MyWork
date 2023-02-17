# Author : Andreia Santos
# Programe name: evens.py
# Program description : This program ask the user to guess a number the program has previous saved in one variable


import os
guess=10
trial=0

while trial!=guess:
    
    trial=int(input("Please try to guess the number the script has hiden "))

    if trial == guess:
        print (f"\nWell done! You got the number right, indeed was the number {trial}")
        break
    
    print("\nNumber wrong. Please try again!\n")
    
    os.system('cls||clear')
   


