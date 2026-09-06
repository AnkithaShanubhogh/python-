from datetime import datetime

name = input("enter your name:")
year_of_birth = int(input("enter your year of birth:"))

current_year = datetime.now().year

age = current_year - year_of_birth 

if age >=60:
    print(f"{name} , you are {age} years old . you're a senior citizen " )

else:
    print(f"{name} , you are {age} years old . you're not a senior citizen ")  

