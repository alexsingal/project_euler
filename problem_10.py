'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

'''

#create a sieve of eratosthenes function which returns all primes up to a value n

def sieve(n):
  m = n+1
  numbers = [True] * m
  for i in range(2, int(n**.5)):
    if numbers[i]:
      for j in range(i*i, m, i):
        numbers[j] = False
  primes = []
  for i in range(2, m):
    if numbers[i]:
      primes.append(i)
  return primes

primes = sieve(2000000)
print sum(primes)
