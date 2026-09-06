num_str=input("enter a multi-digit number")

frequency={}

for digit in num_str:
    if digit.isdigit():
        frequency[digit]=frequency.get(digit,0)+1

print("\n--Digit frequency---")
for digit,count in sorted(frequency.items()):
    print("Digit",digit,"occurs",count,"times")
