# Author : Andreia Santos
# Programe name: lab7.2.py
# Program description :Read info from file modify it and save it again.If the file does not exist create it
# 

import os.path

FILENAME="count.txt"


if os.path.exists(FILENAME):
    print ("File is already there. No need to create")
else:
        print ("File is not on the directory, so it will be created with a starting value of 0")


        f = open("count.txt", "x") # Once the file is not on the directory it will be created


        with open(FILENAME, "wt") as f2:
             f2.write("0") # Insert the value 0 on the file once it is created
  




with open(FILENAME) as f:

    total_old= int(f.read()) # Atention to this in particular, need to convert the string into number so we can increment it
 


total_old=total_old+1


with open(FILENAME, "wt") as f2:

   f2.write(str(total_old)) # Atention to this in particular, need to convert the number into string so it can be saved on the file
  

# Print what at last was saved on the file

with open(FILENAME) as f:

    total_old= int(f.read())
    print("\n\n\nThe saved number on the file will be {}, correspondent to the number of the times this program has been run\n\n\n".format(total_old))




