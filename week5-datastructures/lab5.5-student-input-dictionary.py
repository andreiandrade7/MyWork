# Author : Andreia Santos
# Programe name: student-input-dictionary.py
# Program description : handles dictionaries data, re-access input data functions


student={"name":"begin"} # initialization of key name on dictionary student with the value "begin". Important for the while loop



laster=student.copy() # copy the dictionary to a temporary one-later dectionary - for showing on the print operations


while student["name"]!="":
 
  laster=student.copy()
  student={"name":input("\nInsert the name:")} # name insertion by the user
  
  
  # print to inform the user that no more information will be asked once a empty input was given
  if student["name"]=="":
   print("\n\n\n\nNo more names inserted\n\n\n\n\n\nPROGRAM EXIT!\n\n\n\n") 
   break

# fill the other dictionary information regarding the modules and the respective grades
  student.update(
    {
          "modules":
    

         [
         {
          "coursename":input("Insert the module name: "),
           "grade": int(input("Insert the grade: "))
          },
         {
          "coursename":input("Insert the module name: "),
          "grade": int(input("Insert the grade: "))
        }
        ]
  })

    
    



    #---------------------------------------------------PRINT the last name/grades/modules inserted by the user

print("\n\nThis is the dictionary composition:\n\n")
print("The name you have selected is {}".format(laster["name"])) 
print("The dictionary key is: {}".format(laster.keys())) # prints the composition of the dictionary - titles and values
print("The dictionary value is: {}".format(laster.values())) # prints the the values that are on . NOT the titles!!!
print("The itens on the dictionary are: {}".format(laster.items())) # prints the composition of the dictionary - titles and values
print("The lenght of the dictionary is: {}".format(len(laster)))
print("\n\n")

