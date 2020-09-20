#4-Prime Factorization - Have the user enter a number and find all Prime Factors (if there are any) and display them.



import math
# prime
def primeFactors(n):
   # no of even divisibility
   while n % 2 == 0:
      print (2),
      n = n / 2
   # n reduces to become odd
   for i in range(3,int(math.sqrt(n))+1,2):
      # while i divides n
      while n % i== 0:
         print (i)
         n = n / i
   # if n is a prime
   if n > 2:
      print (n)
n = int(input())
primeFactors(n)

