#7. Prime Numbers 
# A prime number is a number that is only evenly divisible by itself and 1. 
# For example, the number 5 is prime because it can only be evenly divided by 1 and 5. The number 6, 
# however, is not prime because it can be divided evenly by 1, 2, 3, and 6. 
# Write a Boolean function named is_prime which takes an integer as an argument and returns True if the argument is a prime number, 
# or False otherwise. Use the function in a program that prompts the user to enter a number and then displays a message indicating 
# whether the number is prime. 

def input_is_prime (x):
    if x <2:
        return False
    for y in range (2,x):
        if x % y == 0:
            return False
    return True

t = 0 
while t < 1:
    input_number = int(input("please input a integer: "))
    print("Input is a prime number:", input_is_prime(input_number))


