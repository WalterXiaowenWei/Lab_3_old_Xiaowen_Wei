#Write another program that displays all of the prime numbers 
# from 1 through 100.
def input_is_prime (x):
    if x <2:
        return False
    for y in range (2,x):
        if x % y == 0:
            return False
    return True

for x in range (2, 101):
    if input_is_prime(x) is True:
        print (x)
