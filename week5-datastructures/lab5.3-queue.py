# Author : Andreia Santos
# Programe name: queue.py
# Program description : Create 10 random numbers and take individually each number from the set

import random 
total=10

list_random=[]
for x in range (0,total):
     list_random.append(random.randint(1, 100))

print(f"Queue is : {list_random}")


for y in range (0,total):

    print(f"Current number is {list_random.pop(0)} and the queue is {list_random}")



print("the queue is not empty")

# answert to the question 

#the following code line does not print correctly because we are missing the "f". 
#print ("current Number is {currentNumber} and the queue is {queue} ")

#correctly:

# print (f"current Number is {currentNumber} and the queue is {queue} ")