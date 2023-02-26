# Author : Andreia Santos
# Programe name: student-dictionary
# Program description : Familiarization with dictionaries format

student={

    
    "name":"Mary",

    "modules": 
         [
         {
          "coursename":"programing",
           "grade": 45
          },
         {
          "coursename":"history",
          "grade": 99
        }
          ]

}

print("Student:{}".format(student["name"]))

for module in student["modules"]:
    print("\t {} \t:{}".format(module["coursename"], module["grade"]))