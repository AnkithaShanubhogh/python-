num1=float(input("enter a first  number: "))
num2=float(input("enter a second number: "))

print("---choose an operation---")
print("1.Add")
print("2.Substract")           
print("3.multiply")           
print("4.Divide")

choice=int(input("Choose an operation(1-4):"))

if choice == 1 :
    result = num1 + num2
    print(f"Result:{num1} + {num2} = {result}")

elif choice == 2:
    result = num1 - num2
    print(f"Result:{num1} - {num2} = {result}")

elif choice == 3 :
    result = num1 * num2
    print(f"Result:{num1} * {num2} = {result}")

elif choice == 4:
    if num2 != 0:
        result = num1 / num2
        print(f"Result:{num1} / {num2} = {result}")
    else:
        print("Error:Division by zero")    
else:
    print("Invalid choice please enter a number between (1-4)")
    
    

           
           
