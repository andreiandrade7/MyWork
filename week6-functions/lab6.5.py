
# Author : Andreia Santos
# Programe name: lab6.5.py
# Program description : create a student management program [step 5]- insert new modules: 


modules=[]


def readModules():
    Name="test"
    

    while Name != "":
            newModule={}
            Name=input("Insert the module name : ").strip()

            newModule["name"]=Name # it is necessary to create this "Name" variable for being used on the "while" loop
        

            if (Name !=""): # In case the user do not enter any other module program should not ask for the mark
                newModule["mark"]=int(input("Insert the module mark : "))
            

            modules.append(newModule) # add new module with mark info to the dictionary module
    
    return modules



readModules()
print(modules)