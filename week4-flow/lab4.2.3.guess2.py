# Author : Andreia Santos
# Programe name: evens.py
# Program description : This program ask the user to guess a number the program has previous saved in one variable. Also give a hint to the user saying if the number he inserted is higher or lower than the expected


guess=10
trial=0

while trial!=guess:
    
    trial=int(input("Please try to guess the number the script has hiden "))

    if trial == guess:
        print (f"\nWell done! You got the number right, indeed was the number {trial}")
        break
    elif trial>guess:
            print(f"The number you have inserted is higher than the hidden one. Try a number lower than {trial}")
    else:
           print(f"The number you have inserted is lower than the hidden one. Try a number higher than {trial}")
    
    
   

