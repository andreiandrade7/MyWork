# Author : Andreia Santos
# Programe name: evens.py
# Program description : This program ask the user to guess a number that the program has randomly generated. Also give a hint to the user saying if the number he inserted is higher or lower than the expected

import random

guess=random.randint(0, 100) # generate a randon number between 0 and 100

print("Please do not tell anyone, but the number the script have generated was: {}".format(guess))

trial=0


if trial==guess:
    print("Ups! Aparently the random algoritm could not go as far as {trial}\n\n\n\n\n")

while trial!=guess:
    
    trial=int(input("Now, it is your time for trying to guess. Please insert a number: "))

    if trial == guess:
        print (f"\nWell done! You got the number right, indeed was the number {trial}")
        break
    elif trial>guess:
            print(f"The number you have inserted is higher than the hidden one. Try a number lower than {trial}")
    else:
           print(f"The number you have inserted is lower than the hidden one. Try a number higher than {trial}")
    
    
   