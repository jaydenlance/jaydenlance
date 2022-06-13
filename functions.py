#!/usr/bin/python


############################
#        functions in python
#        Name:Lance
#        DAte:31/5/2022

####################

#defining a function 


def say_hello():
    print("hello from Lance")
    

say_hello()


def bark():
    print("Dogs bark whooof whoof")
bark() 

def mows():
    print("Cow mows mooo moooo")
mows()


def crys():
    print("Jabir crys uuuui uuuuui")
crys()    


#Functions parameters

def add_numbers(x,y):
    sum_nums = x + y
    print("The sum of numbers",sum_nums)


add_numbers(40,50)
add_numbers(100,400)
add_numbers(1,4)


#functions to multiply 2 numbers
def prod_numbers(x,y):
    prod_nums = x * y
    print("The prod of numbers",prod_nums)

prod_numbers(40,50)    
prod_numbers(100,400)
prod_numbers(1,4)





#using a default parameter


def print_name(name="Lance Jayden"):
    print(name)