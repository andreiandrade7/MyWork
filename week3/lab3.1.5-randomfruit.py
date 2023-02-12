# Author : Andreia Santos
# Programe name: randomfruit.py
# Program description : Program that randomly generate a fruit on a list of fruits 


import random

fruits = ['Apple', 'Orange', 'Banana', 'Pear']

len(fruits)
generator=random.randint(0,len(fruits)-1)


random=fruits[generator]
print("The fruit selected is {}".format(random))