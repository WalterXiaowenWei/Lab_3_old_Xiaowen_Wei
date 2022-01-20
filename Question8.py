#8. Future Value
#Suppose you have a certain amount of money in a savings account that earns compound monthly interest and you want to calculate the amount that you will have after a specific number of months. The formula is
#F = P * (1 + i) **t
#The terms in the formula are as follows:
#• F is the future value of the account after the specified time period.
#• P is the present value of the account.
#• i is the monthly interest rate.
#• t is the number of months.
#Write a program that prompts the user to enter the account’s present value, monthly interest rate, and number of months that the money will be left in the account. The program should pass these values to a function that returns the future value of the account after the specified  number of months. The program should display the account’s future value.

t = 0 
while t < 1:
    P = float(input("Please input the present value of the account: "))
    i = float(input("Please input the monthly interest rate: "))
    t = float(input("Please input the number of months: "))
    F = P * (1 + i) **t
    print("The account's future value is: ", F)
