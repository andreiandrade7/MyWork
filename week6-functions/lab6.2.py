
# Author : Andreia Santos
# Programe name: lab6.2.py
# Program description : create a student management program [step 1]: receive only the user choice



def menu():
    print ("What would you like to do?\n")
    print ("(a) Add new student\n(v) View students\n(q) Quit\n")
    print ("Type one letter (a/v/q):")
    choose=input()
    
    
    print ("you choose {}".format(choose))
    return choose

option=menu()


