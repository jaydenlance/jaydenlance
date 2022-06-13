#!/usr/bin/python


############################
#        quadratic eqn in python
#        Name:Lance
#        DAte:31/5/2022

####################
#a coefficient of first term
#b coefficient of second term
#c is the constant
#c 



from math import sqrt

a = int(input("Enter the coefficient of first term(a)"))
b = int(input("Enter the coefficient second term(b)"))
c = int(input("Enter the constant(c)"))


def find_roots(a,b,c):
    y_1 = (-b + w) / (2*a)
    y_2= (-b - w) / (2*a)
    print("The roots of the quadratic equations are : ",y_1,y_2)
find_roots(a ,b ,c )   

   
#!usr/bin/python

##########################
#      QUADRATIC EQUATIONS
#      Name: Lance Jayden
#      Date: 31/5/22 
###########################

import math 
a = int(input("Enter the coefficient of the first term."))
b = int(input("Enter the coefficient of the second term."))
c = int(input("Enter the constant."))
def findRoots(a,b,c):
    y1 = ((-b) + math.sqrt ((b**2) - (4*a*c)) ) /(2*a)
    y2 =((-b) - math.sqrt ((b**2) - (4*a*c)) ) / (2*a)
    print("The roots of the quadratic equation are",y1,y2)
findRoots(a,b,c)

# an easier way
import math 
a = int(input("Enter the coefficient of the first term."))
b = int(input("Enter the coefficient of the second term."))
c = int(input("Enter the constant."))
w = int(math.sqrt( (b**2) - (4*a*c) ))
def findRoots(a,b,c):
    y_1 = (-b - w)/ (2*a)
    y_2 = (+b - w)/ (2*a)
    print("The roots of the quadratic equation are",y_1,y_2)
findRoots(a,b,c,w)