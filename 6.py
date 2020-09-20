
#6-Change Return Program - The user enters a cost and then the amount of money given. The program will figure out the change and the number of quarters, dimes, nickels, pennies needed for the change.
import math
cent=0.01
penny=0.01
nickel=0.05
dime=0.1
quarter=0.25
do=1
cost=float(input("Enter the costt"))
amount=float(input("Enter amount paid"))
if cost>amount:
    change=cost-amount
    s=round((change/cent),2)
    p=round((change/cent),2)
    n=round((change/nickel),2)
    d=round((change/dime),2)
    q=round((change/quarter),2)
    de=round((change/do),2)
    print("U can pay ur left amount by paying",s,"cents OR ",p,"pennies OR ", n,"nickels OR", d,"dimes OR",q,"quarters OR", de,"dollars" )
elif amount>cost:
    change=amount-cost
    
    if change>0:
        s=round((change/cent),2)
        p=round((change/cent),2)
        n=round((change/nickel),2)
        d=round((change/dime),2)
        q=round((change/quarter),2)
        de=round((change/do),2)
        print("How would you like to have your change",(s),"cents \n OR \n",p,'pennies \n OR \n"',n,"nickels \n OR \n",d,"dimes \n OR \n",q,"quarters \n OR \n",de,"dollars")
        
elif cost==amount:
    print("Thanks for your purchase \n change left=0")'''

#-Print hex oct......
'''number=int(input())
width = len('{:b}'.format(number))
for i in range(1,number+1):
    print(str.rjust(str(i),width),str.rjust(str(oct(i)[2:]),width),str.rjust(str(hex(i).upper()[2:]),width),str.rjust(str(bin(i)[2:]),width))
