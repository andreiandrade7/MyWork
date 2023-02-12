
# Author : Andreia Santos
# Programe name: lab3.1.6-extra6.py
# Program description : Find and correct the errors and answer questions

# ------------------------------------------------
#question 6
# ------------------------------------------------

# Q: Why does this expression cause an error? How can you fix it? 
    #message = 'I have eaten ' + 99 + ' burritos.'
    #print (message)

    # ANW: 
    # The concatenate function can only work for strings, 99 was a int. It is then necessary to convert is to string

message = 'I have eaten ' + str(99) + ' burritos.'
print (message)



# ------------------------------------------------
#question 7
# ------------------------------------------------

    # Q:
    #Why is eggs a valid variable name while 100 is invalid? 

    # ANW: 
    #There are a set of rules that must be respected for being considered as a variable. One of this rules is NOT starting by a number. Thus 100 is considered invalid


# ------------------------------------------------
#question 8
# ------------------------------------------------

    # Q:
    # What three functions can be used to get the integer, floating-point number, or string version of a value?

    # ANW:
    #The functions to get each individual type are the following (being the x the value:)
    # integer = int(x)
    # float-point number = float (x)
    # value=str(x)