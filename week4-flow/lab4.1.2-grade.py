# Author : Andreia Santos
# Programe name: grade.py
# Program description : This program reads a mark inserted by the user and give it the correspondent grade accordingly

percentage=0
  
while percentage <=0 or percentage >100:
    percentage=int(input("Enter the percentage "))


if percentage < 41:
    print("Fail")
elif percentage < 50:
    print("Pass")
elif percentage < 60:
    print("Merit 2")
elif percentage < 70:
    print("Merit 1")
else:
    print("Distinction")