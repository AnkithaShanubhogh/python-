num=int(input("Enter a number:"))

first_number=0
second_number=1

if num <=0:
    print("Please enter a positive number")
elif num == 0:
    print("Fibonacci series:",first_number)
else:
    print("Fibonacci series:",first_number,second_number,end=' ')
    for i in range (2, num):
        next_number=first_number + second_number
        first_number=second_number
        second_number=next_number
        print(next_number,end=' ')
