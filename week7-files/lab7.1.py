# Author : Andreia Santos
# Programe name: lab7-1py
# Program description :quizz



# no python program is created here- Answer to a quizz exclusively


#######################################################################################   ANSWERS


#1 a
#ANWS: nothing is printed . It will surge an error on the terminal saying that the file does not exists (errorno2). When the operator is omitted 
       #the predefined operation is to read. Once there in no file with such a name, a error is given

#1b 
#ANWS: If we do not use the "for" loop there will be no output of the file. Only the no. of characters within the file. In this case the output will be 7 (f1 file) and 13 (f2 file)


#1c
#ANS: Will only appear "another line". Once on the first f1 file is not used an "a" instead which per si would append the data. The replacement would not happen

#1c
#ANS: Will only appear "another line". Once on the first f1 file is not used an "a" instead which per si would append the data. The replacement would not happen

#1d
#ANS: Once the append "function" was used on the momment the opening the file,  the output will be:
    # test d
    # another line


 



#######################################################################################   CODE


"""
######################## a code


# the with statement will automatically close the file
# when it is finished with it

with open("test-a.txt") as f:
    data = f.read()
    print (data)

# the old way of doing this is
# f = open ("test1.txt")
# data = f.read()
# print(data)
# f.close()




######################## b + c code


with open("test-b.txt", "w") as f:
    data = f.write("test b\n") # returns the number of chars written
    print (data)

with open("test-b.txt", "w") as f2: # open file again
 data = f2.write("another line\n")
 print (data)




######################## d code


with open("test-d.txt", "w") as f:
    data = f.write("test d\n") # returns the number of chars written
    print (data)


with open("test-d.txt", "a") as f2: # open file again
    data = f2.write("another line\n")
    print (data)


"""