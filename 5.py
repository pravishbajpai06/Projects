#5- Next Prime Number - Have the program find prime numbers until the user chooses to stop asking for the next one.
n=int(input())
i=1
l=[]
for k in range(1,n+1):
    c=0
    for j in range(1,i+1):
        if i%j==0:
            c=c+1
        
    if c==2:
        l.append(i)
        
    i=i+1        
print(l)
for i in range(n):
    print("do you want to get the next prime number:  Enter y or n")
    a=input()
    if a=="y":
        print (l[i])
    elif a=="n":
        break

