# Author : Andreia Santos
# Programe name: months-tupple
# Program description : Create a tupple with the name of the months. From this previous tupple generate e new one with only the summer months



all_months=("January",
"February",
"March",
"April",
"May",
"June",
"July",
"August",
"September",
"October",
"November",
"December")

# a tupple similar to what happen with a list starts in index 0. So for having the summer month we should start on 4 position.
summer=all_months[4:7] # it takes the variable type of its parent (all_months)


for x in summer:
    print(x)
