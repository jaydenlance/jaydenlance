#!/usr/bin/python

##################
#      file operations
#      Name : Lance Jayden 
#      Date : 23/5/2021
##########
f = open("lesson.txt",)
f = open("lesson1.txt","x")
#reading a file
print(f.read())
f.close()

#opening file
with open ("Lesson1.txt",'w'):
    f.Write ("This is my first text file that has been created\n")
    f.Write ("I am from Nandi but i currently reside in Nairoby\n")
    f.Write ("Today is a chilly day and people are freezing\n ")
print (f.readline())