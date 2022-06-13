








#using a default parameter


def print_name(name="Lance Jayden"):
    print(name)

print_name("Jayden")    



#return from a function

def get_sum(num1 , num2):
    sum_nums = num1 + num2
    return sum_nums

print(get_sum(7,12))


#spuare of numbers

def powers (number , power):
    power_numb = number**power
    return power_numb
powers(6,4)
print(powers)


def get_full_name(f_name,s_name):
    full_name = f_name + "" + s_name
    return full_name.title()

print(get_full_name("Lance","Jayden"))

#Returning a dictionary from a function 

def create_full_name(first_name,second_name):
    person = { 'first_name': first_name,'second_name':second_name}
    return person

student = create_full_name('Lance','Jayden')
print(student)

#passing a list in a function

def greet_friends(names):
    for name in names :
        msg = " Hello "  +  name.title() + "!"
        print(msg)   

friends = ['Margie','Jabir','Lance','Lawi','Steph']    
greet_friends (friends)