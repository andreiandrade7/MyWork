
# Author : Andreia Santos
# Programe name: lab7.5.py
# Program description : add the function save in the menu (function not active yet- next exercise)

#------------------------------------------------------------------------------
# 1 . Functions set up
#------------------------------------------------------------------------------

# Function menu

def menu():
    print ("What would you like to do?\n")
    print ("(a) Add new student\n(v) View students\n(s) Save students\n(q) Quit\n")
    choose = input("Type one letter (a/v/s/q): ").strip()
    
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

            newModule["nameModule"]=Name # it is necessary to create this "Name" variable for being used on the "while" loop
        

            if (Name !=""): # In case the user do not enter any other module program should not ask for the mark
                newModule["markModule"]=int(input("Insert the module mark : "))
            

            modules.append(newModule) # add new module with mark info to the dictionary module
    
    return modules






# Function for vizualizing all students

def doview(students):

    print("selected VIEW")
    print(type(students))

    for currentStudent in students: 
            print(currentStudent["name"])
            displayModules(currentStudent["modules"])



def displayModules(modules):
    print("\tModules", "\tMarks")

    for module in modules:
        print("\t{}".format(module["markModule"]))





def displayModules(modules):
    print ("\tName \tGrade")
    
    for module in modules:
    

        print("\t {} \t:{}".format(module["nameModule"], module["markModule"]))


def doView(students):

    for currentStudent in students:
        print(currentStudent["name"])
        displayModules(currentStudent["modules"])




#------------------------------------------------------------------------------
# 2 . Variables set up
#------------------------------------------------------------------------------

students=[]

#------------------------------------------------------------------------------
# 3 . Execution
#------------------------------------------------------------------------------

option=menu()



while (option != "q"):
   
    if option=="a":
        doAdd(students)
        
        print ("perform a")
        

    elif option=="v":
        doView(students)
        print ("perform v")
        
    elif option=="s":
        doSave(students)
        print ("perform s")

    elif option != "q":
         print ("Please keep to the available options, select: a, v or q")
    
    option=menu()
    print("END")











        

        

