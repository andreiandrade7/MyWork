
# Author : Andreia Santos
# Programe name: lab6.4.py
# Program description : create a student management program [step 4]- create a new student: 

students=[]

def doAdd(students):
    newstudent={} 
    newstudent["name"]=input("Insert the student name for the new student: ")
    #newstudent["modules"]=readModules() # once user can insert more than one module at the same time is neater to generate a new function:readModule() - next lab step

    students.append(newstudent) # add to the already defined data-dictionary- a new student with modules information

    

doAdd(students)
print (students)




        

        

