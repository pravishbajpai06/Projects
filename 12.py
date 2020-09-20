#12-Happy Numbers - A happy number is defined by the following process. Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers, while those that do not end in 1 are unhappy numbers. Display an example of your output here. Find first 8 happy numbers.


    
def sumsquare(number):
    s=0
    while number!=0:
        a=number%10
        s+=a*a
        number=number/10
    return s
def happynum(number):
    s=set()
    s.add(number)
    while True:
        if number==1:
            return True
        number=sumsquare(number)
        if number in s:
            return False
        s.add(number)
    return False
n=int(input("Enter your number"))
if happynum(n):
    print("yes")
else:
    print("No")
