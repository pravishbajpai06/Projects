
#1-Find PI to the Nth Digit - Enter a number and have the program generate π (pi) up to that many decimal places. Keep a limit to how far the program will go.


from math import pi
x=int(input())
print("{:.{}f}".format(pi, x))
