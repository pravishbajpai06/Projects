#20-Coin Flip Simulation - Write some code that simulates flipping a single coin however many times the user decides. The code should record the outcomes and count the number of tails and heads.
import random
n=int(input("How many tims do you want to flip the coin"))
h=0
t=0
for i in range(1,n+1):
    flip=random.choice(["h","t"])
    print(flip)
    if flip=="h":
        h+=1
    elif flip=="t":
        t+=1
print("no. of times tails came is",t)
print("no. of time heads came is",h)
