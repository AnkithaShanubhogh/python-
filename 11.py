marklist=[]

print("Enter marks for 6 subjects :")

for i in range(6):
    mark=float(input(f"enter mark for subject{i+1}:"))
    marklist.append(mark)

n=len(marklist)
for i in range(n-1):
    for j in range (n-i-1):
        if marklist[j]<marklist[j+1]:
               marklist[j],marklist[j+1]=marklist[j+1],marklist[j]

print("\n---Student marks report---")
print("marks sorted from highest to lowest:")
for mark in marklist:
    print(mark)


