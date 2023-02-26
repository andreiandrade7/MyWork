# Author : Andreia Santos
# Programe name: quizz
# Program description : This program is a quizz for acessing the knowing regarding the variables types


numberOfQuestions = 5
averageAge = 23.4
debugMode = True
name = "joe"
ages = []
months = ('Jan', 'Feb', 'Mar')
book = {}
stuff = [ 12 , 'Fred', False, {}]
someone = dict(firstname = "joe")


me = {
"firstName" : "Andrew",
"teaching" : [{
"courseName" : "programming",
"semester" : 1
},{
"courseName" : "Data Representation",
"semester" : 2
}
]
}

print(type(me["teaching"][0]["coursename"]))

"""
--------------------------------------------------------------------------- QUIZ QUESTIONS/ANSWERS


a. numberOfQuestions
    int

b. averageAge
    lfoat

c. debugMode
    boolean

d. name
    string


e. ages
    list

f. months
    tupple

g. months[1]
    string


h. book
        dictionary

        
i. stuff
    list

j. stuff[2]
    Boolean - cerefully because list on the "index no.0"

k. someone
    dictionary

l. someone["firstname"]
    string

m. me
    dictionary

n. me["teaching"]
    list

o. me["teaching"][0]["semester"]
    int

p is a trick question look at it carefully


p. me["teaching"][0]["coursename"]
    undefined because the variable has a capital N on the "coursename"

"""