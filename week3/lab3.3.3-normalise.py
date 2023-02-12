# Author : Andreia Santos
# Programe name: normalise.py
# Program description : Return the trimmed version of one user inserted screen (ignore empty spaces in the beginning if any) and replace the upper cases by lower case



stringInput=input("Please insert the string:")


cleanSpaces=stringInput.strip()

normalize=cleanSpaces.lower()

print("That string normalized is:{}".format(normalize))


print("We reduce the input string from {} to  {} characters".format(len(stringInput),len(normalize)))
