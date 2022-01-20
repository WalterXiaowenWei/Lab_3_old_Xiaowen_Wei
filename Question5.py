#5. Pennies for Pay
# Write a program that calculates the amount of money a person would earn over a period of time if his or her salary is one penny the first day, 
# two pennies the second day, and continues to double each day. The program should ask the user for the number of days.
# Display a table showing what the salary was for each day, and then show the total pay at the end of the period. The output should be displayed 
# in a dollar amount, not the number of pennies.

t = 0 
while t < 1:
    payment_day = int(input("Please input the total days of working: "))
    firstDay_payment = 0.01 
    if payment_day == 1:
        print ("day","             ","Income (dollar)")
        print ("1","               ","0.01")
        print ("Your total income (dollar): 0.01")
    elif payment_day == 0:
        print ("day","             ","Income (dollar)")
        print ("0","               ","0.00")
        print ("Your total income (dollar): 0.00")
    else:
        print ("day","             ","Income")
        print ("1","               ","0.01")
        total_payment = 0.01
        for x in range (1, payment_day):
            firstDay_payment = firstDay_payment*2
            total_payment = total_payment + firstDay_payment
            print(int(x+1),"               ", firstDay_payment)
        print ("Your total income (dollar): ", total_payment)
