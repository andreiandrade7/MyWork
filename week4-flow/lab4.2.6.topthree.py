# Author : Andreia Santos
# Programe name: evens.py
# Program description : This program randomly generate numbers- total amount inserted by the user- and show the top 3 of this list

import random

list_raw=[]
list_orde=[]
list_top=[]
rand_numb=0
posi=0

print("\n\n\n\n\n----------------------------------------------  USER INPUT ----------------------------------------------")
total=int(input("\n\nInsert the number of elements you would like to generate\n\n"))
amount_shown=int(input("\n\nHow many top numbers would you like to shown?\n\n"))



print("\n\n\n\n\n----------------------------------------------  SCRIPT OUTPUT ----------------------------------------------\n\n\n")


for x in range(0,total):
    
    rand_numb=random.randint(0,100)
    list_raw.insert(x, rand_numb)

print(f"The generated list is: {list_raw}\n\n")

list_raw.sort(reverse=False)


print(f"The list ordered is: {list_raw}\n\n")






for a in range(1,amount_shown+1):

    posi=len(list_raw)-a
    list_top.append(list_raw[posi])


print(f"The {amount_shown} top numbers from the list are: {list_top}\n\n")