#2-Find e to the Nth Digit - Just like the previous problem, but with e instead of π (pi). Enter a number and have the program generate e up to that many decimal
#places. Keep a limit to how far the program will go.


from math import e
x=int(input())
print(round(e,x))
