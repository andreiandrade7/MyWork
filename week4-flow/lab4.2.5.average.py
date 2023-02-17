# Author : Andreia Santos
# Programe name: evens.py
# Program description : This program estimate a average of a set of inserted numbers. The insertion of the numbers stop once the user uses -1 as input. 
 #                      Used two different method:
#                           1. Using numpy
#                           2. Using only the list                

import numpy

list_avera=[]
average=0

stopper=-1
number=0


while number != stopper:

    number=int(input("Please insert a number. Or either insert -1 if you want to quit "))

    if number != stopper:
        list_avera.append(number)

else:
    """
    #               method 1 - using numpy
    average=numpy.mean(list_avera)
    print (f"The average of the list {list_avera}  is {average}")
"""
    #               method 2 - using the list

    average=float(sum(list_avera)/len(list_avera))

    print (f"The average of the list {list_avera}  is {average}")

