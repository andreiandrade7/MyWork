# Author : Andreia Santos
# Programe name: grade.py
# Program description : Extra exercises-3


# method 1
#ANS: round the insertedpercentage to the lower position


# method 2
#ANS: 
percentage=0
  
while percentage <=0 or percentage >100:
    percentage=int(input("Enter the percentage "))


if percentage < 41:
    print("Fail")
elif percentage < 50:
    print("Pass")
elif percentage < 60:
    print("Merit 2")
elif percentage < 71: # change 70 to 71
    print("Merit 1")
else:
    print("Distinction")