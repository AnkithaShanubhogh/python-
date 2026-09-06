#Lab Program 2. a.
#Develop a program to generate Fibonacci sequence of length (N). Read N from the console.

'''Enter a number: __    # >1
   Fibonacci Series:_ _ _ _
   
   Enter a number: __   #less than 0 if entered
   please enter positive number
   
   Enter a number: 1
   Fibonacci Series: 0     '''

num=int(input("Enter a number:"))
first_number=0
second_number=1
next_number=first_number + second_number

if num <= 0:
    print(" Please enter a positive number:" )

elif num == 1:
    print(" Fibonacci series:0")

else:
    print(" Fibonacci series:",first_number,second_number , end=' ')
    for i in range(2,num):
        next_number=first_number + second_number      # 0,1 => next_number=0+1 ..> 1
        first_number=second_number
        second_number=next_number
        print(next_number,end=' ')
    
