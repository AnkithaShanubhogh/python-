import math

N = int(input("how many numbers do you want:"))
numbers = []
for i in range(N):
    num = float(input(f"enter the number{i+1}:"))
    numbers.append(num)

mean = sum(numbers)/N
variance = sum((x-mean)**2 for x in numbers)/N
std_dev = math.sqrt(variance)

print("---Results---")
print(f"Numbers:{numbers}")
print(f"Mean={mean}")
print(f"Variance={variance}")
print(f"Standard_deviation={std_dev}")
