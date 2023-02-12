# Author : Andreia Santos
# Programe name: randomGenerator.py
# Program description : Program that randomly generate a number a lower and upper limit (defined by the user)



import random


lower=int(input("The following script randomly selects a number within a given range \n\nPlease define the lower limit of the range:"))
upper=int(input("Please define the upper limit of the range:"))


generator=random.randint(lower,upper+1)

print ("The number randomly generated was {} ".format(generator))