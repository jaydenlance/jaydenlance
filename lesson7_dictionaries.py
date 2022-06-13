#      name:Lance
#      Date : 23 / 5 / 2021
##########################


#Initializing dictionaries
student = { "Name": "Lance","age":18,"gender":"male"}
print(student,["Name"],["age"],["gender"])

#Adding key value to dictionary
student["Id-No"] = "23631550"
student["Hobby"] = "reading"
student["club"] = "Chelsea"
student["Favourite movie"] = "Red Notice"
print(student)

#Empty dictionary
student ={}
student["favourite food"] = "Pizza"
student["home_city"] = "Nandi"
print(student)

#Modifying values in a dictionary
student["Name"] = "Jayden"
student["age"] = "19"
student["club"] = "Liverpool"
student["favourite food"] = "chips"
print(student)

#how to del in a dictionary
del student["favourite food"]
print(student)