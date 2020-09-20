
#14-Credit Card Validator - Takes in a credit card number from a common credit card vendor (Visa, MasterCard, American Express, Discoverer) and validates it to make sure that it is a valid number (look into how credit cards use a checksum).


n=int(input("Enter your card number"))
l=list(str(n))
length=len(l)


if length <13:
    print("invalid card")
elif length>16:
    print("invalid card")
elif length>=13 and length<=16:
    if length%2!=0:
        for i in range(length):
            if i%2!=0:
                l[i]=int(l[i])*2
        for j in range(length):
            if type(l[j])==str:
                l[j]=int(l[j])

        for k in range(length):
            if l[k]>9:
                s=0
                while l[k]>0:
                    s+=l[k]%10
                    l[k]=l[k]/10
                l[k]=s        
            
    elif length%2==0:
        for i in range(length):
            if i%2==0:
                
                l[i]=int(l[i])*2
        for j in range(length):
            if type(l[j])==str:
                l[j]=int(l[j])

        for k in range(length):
            if l[k]>9:
                s=0
                while l[k]>0:
                    s+=l[k]%10
                    l[k]=l[k]/10
                l[k]=s        


print(l)        
summ=sum(l)
print(summ)
if summ%10==0:
    
    print("Valid")
else:
    print("Invalid card")
