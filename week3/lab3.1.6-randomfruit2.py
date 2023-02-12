# Author : Andreia Santos
# Programe name: randomfruit2.py
# Program description : Modify program no lab3.1.5 for using a tuple instead of a list for the fruits name


import random

fruits = ('Apple', 'Orange', 'Banana', 'Pear')


print("Variable {} is of type: {} and its value is: {}\n\n".format("fruits",type(fruits),fruits))


len(fruits)
generator=random.randint(0,len(fruits)-1)

print("The fruit selected is {}".format(fruits[generator]))

