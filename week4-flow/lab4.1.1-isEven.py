# Author : Andreia Santos
# Programe name: isEven.py
# Program description : This program will inform the user if the number he has introduced is even or odd



user_no=int(input("Please enter a number: "))


if user_no%2==0:
    print("The number {} is even".format(user_no))
else:
    print("The number {} is odd".format(user_no))
