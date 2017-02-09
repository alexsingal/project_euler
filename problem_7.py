'''
Project Euler Problem 7:

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10,001st prime number?

'''

#Prime number test
def isPrime(n):
    if n == 2:
        return True
    if n == 3:
        return True
    if n % 2 == 0:
        return False
    if n % 3 == 0:
        return False

    i = 5
    w = 2

    while i * i <= n:
        if n % i == 0:
            return False

        i += w
        w = 6 - w

    return True


count = 2
i = 5
w = 2
while True :
    if isPrime(i):
        count += 1
    if count == 10001:
        break
    i += w
    w = 6 - w
print i
