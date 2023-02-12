# Author : Andreia Santos
# Programe name: convert.py
# Program description : The following script receive a float number from the user, convert it in an absolute value and convert the same amount in cents. 


input=float(input(("Please insert the amount you would like to convert.\nFollow the format:\t 200.23 - 200 dolars and 23 cents\n Insert number: ")))


# consider the absolut number of the input
inputToAbsolute=abs(input)

# estimate the cents amount
amountCents=inputToAbsolute*100

# converts the cents amount into a integer number and show it on the screen
print("\n\nThe total amount in cents is:{}".format(int(amountCents)))