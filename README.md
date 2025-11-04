# python-
python programs
name=input("enter your name:")             ''' \t  then enter name -->  \t  then prints entered name'''
print(f"hello,{name}")                         

name=input("enter your name:") 
name=name.strip()                          ''' \t then enter name --> directly prints name without giving any space  if we use .strip()'''
print(f"hello,{name}")  

name=input("enter your name:") 
name=name.strip() 
name=name.capitalize()                    ''' capilizes the letters in  name   #Annu shanbhagh '''
print(f"hello,{name}") 


name=input("enter your name:") 
name=name.strip() 
name=name.title()                    ''' capilizes the letters in  name   #Annu Shanbhagh '''
print(f"hello,{name}") 

name=input("enter your name:") 
name=name.strip().title()                  ''' capilizes the letters in  name   #Annu shanbhagh '''
print(f"hello,{name}")   

name=input("enter your name:").strip().title()                    ''' capilizes the letters in  name   #Annu shanbhagh '''
print(f"hello,{name}") 
