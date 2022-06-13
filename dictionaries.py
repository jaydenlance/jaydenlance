#A dictionary is a collection of key value pair .key:value
#syntax : dictionary = {"key" : "value"}



colours = {"colour" : "red"}
vehicle = {"type" : "toyota","plate number":"KBT"}
#print(type(colours)) #we use the type method 
#Acessing values in a dictionary
print(vehicle["type"])#you can access the value of an element 
print(vehicle['type'],vehicle['plate number'])


#dictionary Person
person = {'name':'jayden','gender': 'male','phone_number': '0720271424','adress':'151-200 kamkunji'}
person['age']='22'
print(type(person))
print(person)
del person  ['phone_number']
#looping over dictionaries
#for key , value in person .items():
#  print(f'{key}:{value}') 
#using get to access the value in a dictionary





#lists
mary_fav_food = ['beef','chicken','vegetable']
jane_fav_food = ['rice','ugali','chips']
fav_food ={
    "mary":["beef","chicken","vegetable"],
    "jane":["rice","ugali","chips"]
}
print(fav_food)


for key, value in fav_food.items():
    print(f"{key}:{value}") 


