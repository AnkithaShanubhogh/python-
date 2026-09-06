#Program 1. b.
#Develop a program to read the name and year of birth of a person. Display whether the person is a
#senior citizen or not.
'''Enter     your     name : ____
   Enter your year of birth: ____
   ____, you are __ years old. You are not a senior citizen

   _____, you are __ years old. You are a senior citizen.'''

#step1:

from datetime import datetime

Name=input("Enter your name:")
Year_of_birth=int(input("enter your year of birth:"))

#step2:
current_year = datetime.now().year

#step3:cal age
age = current_year - Year_of_birth
if age >= 60:
    print(f"{Name}, You are {age}year old. Your are a senior citizen ")

else:
    print(f"{Name}, You are {age} year old.you are not a senior citizen ")




