
# Author : Andreia Santos
# Programe name: lab6.6.py
# Program description : create a student management program [step 6] - integrate previous step 4 and 5 into the main function (step 3): 

#------------------------------------------------------------------------------
# 1 . Functions set up
#------------------------------------------------------------------------------

# Function menu

def menu():
    print ("What would you like to do?\n")
    print ("(a) Add new student\n(v) View students\n(q) Quit\n")
    choose = input("Type one letter (a/v/q): ").strip()
    
    print ("you choose {} : \n".format(choose))
    return choose



# Function for adding new students

def doAdd(students):
    newstudent={} 
    newstudent["name"]=input("Insert the student name for the new student: ")
    newstudent["modules"]=readModules() # once user can insert more than one module at the same time is neater to generate a new function:readModule()

    students.append(newstudent) # add to the already defined data-dictionary- a new student with modules information


def readModules():
    modules=[]
    Name="test"
    

    while Name != "":
            newModule={}
            Name=input("Insert the module name : ").strip()

            newModule["name"]=Name # it is necessary to create this "Name" variable for being used on the "while" loop
        

            if (Name !=""): # In case the user do not enter any other module program should not ask for the mark
                newModule["mark"]=int(input("Insert the module mark : "))
            

            modules.append(newModule) # add new module with mark info to the dictionary module
    
    return modules






# Function for vizualizing all students

def doview(students):

    print("selected VIEW")

    



#------------------------------------------------------------------------------
# 2 . Variables set up
#------------------------------------------------------------------------------

students=[]



#------------------------------------------------------------------------------
# 3 . Execution
#------------------------------------------------------------------------------

option=menu()



while option != "q":
    print("I was here")
    if option=="a":
        doAdd(students)
        
        print ("perform a")
        option=menu()

    elif option=="v":
        doview(students)
        print ("perform v")
        option=menu()
        
    elif option != "q":
         print ("Please keep to the available options, select: a, v or q")
         option=menu()
    print("END")
    break











        

        

