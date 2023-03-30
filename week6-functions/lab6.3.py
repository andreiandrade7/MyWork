
# Author : Andreia Santos
# Programe name: lab6.3.py
# Program description : create a student management program [step 3]: 

#------------------------------------------------------------------------------
# 1 . Functions set up
#------------------------------------------------------------------------------

# Function menu
def menu():
    print ("What would you like to do?\n")
    print ("(a) Add new student\n(v) View students\n(q) Quit\n")
    print ("Type one letter (a/v/q):")
    choose=input().strip()
    
    print ("you choose {}".format(choose))
    return choose


option=menu()


#------------------------------------------------------------------------------
# 2 . Execution
#------------------------------------------------------------------------------


while option != "q":
    print("I was here")
    if option=="a":
        #doAdd()
        
        print ("perform a")

    elif option=="v":
        # doview()
        print ("perform v")

    elif option != "q":
         print ("Please keep to the available options, select: a, v or q")
         option=menu()
    print("END")
    break






