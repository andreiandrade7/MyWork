# Author : Andreia Santos
# Programe name: grade.py
# Program description : Extra exercises-4. This program will inform the user is inserting odd or even number. Stopps running whtn inserted "-1"

user_no=1

while user_no !=-1:

    user_no=int(input("Please enter a number: "))


    if user_no%2==0:
        print("The number {} is even".format(user_no))
    elif user_no==-1:
        print("\n\n\nProgram stopped\n\n\n")
        break
    else:
        print("The number {} is odd".format(user_no))

    
