# 6. Sum of Numbers
# Write a program with a loop that asks the user to enter a series of positive numbers. 
# The user should enter a negative number to signal the end of the series. After all the positive numbers have been entered,
# the program should display their sum.

print ("please input a number, if it is postive we will add it;")
print ("If it is negative we will stop and calculate the sum of the series of positive number that you input before")

t = 0 
total = 0
while t < 1:
    number_input = float(input("please enter a number: "))
    if number_input > 0:
        total += number_input
    elif number_input < 0: 
        print ("The sum of number: ", total)
        break
    else:
        print ("Error! please input correct number")
    