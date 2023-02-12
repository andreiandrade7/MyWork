# Author : Andreia Santos
# Programe name: Div.py
# Program description : This program receives from the user two values. The First value is divided by the second and on the screen is show the Iinteger and remain result of such division 


input1=int(input("Insert first number: "))
input2=int(input("Insert second number: "))

div=(input1//input2)
remain=input1%input2

print("{} divided by {} is {} with remainder {}".format( input1, input2,div,remain ))
