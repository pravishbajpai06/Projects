#3-Fibonacci Sequence - Enter a number and have the program generate the Fibonacci sequence to that number or to the Nth number.

def fib(n):
    if n<=1:
        return n
    else:
        return(fib(n-1)+fib(n-2))
n=int(input())
if n<=0:
    print("enter positive integer")
else:
    for i in range(1,n+1):
        print(fib(i))
