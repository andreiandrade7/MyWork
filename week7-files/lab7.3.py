# Author : Andreia Santos
# Programe name: lab7.3.py
# Program description :create a json file and insert dictionary data on it

import json

FILENAME="dic-test.json"
sample= dict(name='fred', age=31, grades=[1,34,55])

#create a function that does the conversion from a dictionary into a json file
def writedict(obj):
    

    with open(FILENAME,"wt") as f:
        json.dump(obj,f)


writedict(sample)