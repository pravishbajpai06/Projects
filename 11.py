#11-Tax Calculator - Asks the user to enter a cost and either a country or state tax. It then returns the tax plus the total cost with tax.


def statetax(number):
    s=float(input("Enter your state tax value"))
    st=s*number
    return st
def countrytax(number):
    c=float(input("Enter your country tax"))
    ct=c*number
    return ct
def totaltax(number):
    country=countrytax(number)
    state=statetax(number)
    totaltax=country+state
    return totaltax
n=float(input("Enter your cost"))
print(totaltax(n))
