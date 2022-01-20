#1. Land Calculation
# One acre of land is equivalent to 43,560 square feet. 
# Write a program that asks the user to enter the total square feet in a tract of land and calculates the number of acres in the tract.

x = 0 
while x < 1:
    land_in_squarefeet = float(input("What is the land total area in square feet: "))
    print ("The numberof acres in tract: ", land_in_squarefeet/43560)