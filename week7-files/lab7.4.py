# Author : Andreia Santos
# Programe name: lab7.4.py
# Program description :reading a  dictionary from a jason file


import json

FILENAME="dic-test.json"



#create a function that does the conversion from a dictionary into a json file
def readdict():
    

    with open(FILENAME) as f:
        return json.load(f)


print(readdict())