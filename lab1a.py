# Program 1. a.
# Develop a python program to read 2 numbers from the keyboard and perform the basic arithmetic
#operations based on the choice.
#(1-Add, 2-Subtract, 3-Multiply, 4-Divide).

'''Enter the first number:_ 
Enter the second number:_ 
Choose an operation:_
1. Add
2. Subtract
3. Multiply
4. Divide
Enter your choice (1-4):_ 
Result:_ + _ = _ '''

num1=float(input("enter the first number:"))
num2=float(input("enter the second number:"))
print("/n choose an operation:")
print("1.Add")
print("2.substract")
print("3.multiply")
print("4.divide")
Choice = int(input("enter your choice(1-4):"))
if Choice == 1:
    result = float(num1 + num2 )
    print(f"Result = {num1} + {num2} = {result}")
elif Choice == 2:
    result = float(num1 - num2)
    print(f"Result = {num1} - {num2} = {result}")
elif Choice == 3:
    result = float(num1 * num2)
    print(f"Result = {num1} * {num2} = {result}")
elif Choice == 4:
    result = float(num1 / num2 )
    print(f"Result = {num1} / {num2} = {result}")
else:
    print("Invalid Choice please enter number between 1 and 4.")

    
    








