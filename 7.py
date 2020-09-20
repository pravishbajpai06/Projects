#7- Binary to Decimal and Back Converter - Develop a converter to convert a decimal number to binary or a binary number to its decimal equivalent.
def float_bin(number, places = 3): 
   
    whole, dec = str(number).split(".") 
   
    whole = int(whole) 
    dec = int (dec) 
  
    res = bin(whole)[2:] + "."
  
   
    for x in range(places): 
  
        whole, dec = str((decimal_converter(dec)) * 2).split(".") 
  
        
        dec = int(dec) 
  
        
        res += whole 
  
    return res 
  

def decimal_converter(num):  
    while num > 1: 
        num /= 10
    return num 

def binary(number):
    s=str(number)
    l=list(s)
    g=l[::-1]
    
    s=0
    for i in range(len(g)):
        s=s+(int(g[i])*(2**i))
    
    return("Your binary number is",s)  
 
n=int(input("Enter 1 for decimal to binary or 2 for binary to decimal"))
  

if n==1:
      foi=int(input("Enter 1 for floting point or 2 for integer type"))
      if foi==1:
          number=float(input("Enter your floating point number"))
          p = int(input("Enter the number of decimal places of the result : \n")) 
  
          print(float_bin(number, places = p))
      if foi==2:
          number=int(input("Enter your number"))
          print(bin(number)[2:])

elif n==2:
    number = int(input("Enter your binary number"))
    print(binary(number))'''






#- Another program to calculate decimal to binary





'''k=[]  
def fun(number):
    
    
    if int(number)<=1:
        k.append(int(number))
        
        
        fun(number*2)
        
     
    return(k)

n=float(input())
a=int(n)
b=(n-a)*2

(fun(b))
b=bin(a)[2:]
print(b)
for i in k:
    s=''.join(map(str,k))
print(s)
print(str(b)+"."+s)
