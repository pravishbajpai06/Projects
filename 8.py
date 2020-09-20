#8-Unit Converter (temp, currency, volume, mass and more) - Converts various units between one another. The user enters the type of unit being entered, the type of unit they want to convert to and then the value. The program will then make the conversion.


    
def kelvin_change(val):
    e=int(input("Entr 1 to change from C to K or 2 to change from F to k"))
    if e==1:
        print((val+273.15),"K")
    elif e==2:
        val=(((val-32)*5)/9)+273.15
        print(val)
def fahrenheit_change(val):
    e= int(input("Enter 1 to change from K to F or 2 to change from C to F"))
    if e==1:
        val=((((val-273.15)*9)/5)+32)
        print(val,'F')
    elif e==2:
        val=(((val*9)/5)+32)
        print(val,'F')
def celsius_change(val):
    e= int(input("Enter 1 to change from K to C or 2 to change from F to C"))
    if e==1:
        val=val-273.15
        print(val,'C')
    if e==2:
        val=(((val-32)*5)/9)
        print(val,'C')

def INR_change(val):
    e= int(input("Enter 1 to change from $ to INR or 2 to change from € to INR"))
    if e==1:
        print((val+73.48),'INR')
    elif e==2:
        print((val+87.05),'INR')
def dollar_change(val):
    e= int(input("Enter 1 to change from INR to $ or 2 to change from € to $"))
    if e==1:
        print((val+0.014),'$')
    elif e==2:
        print((value+1.18),'$')
def euro_change(val):
    e= int(input("Enter 1 to change from INR to € or 2 to change from $ to €"))
    if e==1:
        print((val+0.011),'€')
    elif e==2:
        print((val+0.84),'$')
        

n=int(input("Enter 1 for temprature conversion 2 for currency conversion 3 for mass conversion"))

if n==1:
    temp=float(input("Enter the value "))
    q=int(input("Enter 1 to change in K, 2 to change in F, 3 to change in C"))
    if q==1:
        kelvin_change(temp)
    elif q==2:
        fahrenheit_change(temp)
    elif q==3:
        celsius_change(temp)
        

elif n==2:
    curr=float(input("Enter your amount"))
    q=int(input("Enter 1 to change n INR, 2 to change in $, 3 to change in €"))
    if q==1:
        INR_change(curr)
    elif q==2:
        dollar_change(curr)
    elif q==3:
        euro_change(curr)
