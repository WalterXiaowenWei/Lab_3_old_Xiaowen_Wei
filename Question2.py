# 2. Miles-per-Gallon
# A car’s miles-per-gallon (MPG) can be calculated with the following formula:
# MPG = miles travelled / gallons consume
# Write a program that asks the user for the number of miles driven and the gallons of gas used. 
# It should calculate the car’s MPG and display the result.

x = 0 
while x < 1:
    number_of_miles = float(input("the number of miles driven: "))
    gallons_of_gas = float(input("the gallons of gas used: "))
    print("MPG = miles travelled / gallons consume = ", number_of_miles/gallons_of_gas )
