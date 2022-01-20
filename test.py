def isPrime(num):
    if num < 2:
        return False
    for i in range(2,num):
        if num%i==0:
            return False
    return True

print (isPrime (11))


for x in range (2,101):
    for y in range (2,x):
        print(x,y)