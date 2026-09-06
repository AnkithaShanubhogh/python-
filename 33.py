# i) Create a text file and write student names into it
file = open("students.txt", "w")
file.write("Anu\n")
file.write("Ravi\n")
file.write("Priya\n")
file.write("Kiran\n")
file.close()

# ii) Read the file and display all names line by line
file = open("students.txt", "r")
names = file.readlines()

print("Student Names:")
for name in names:
    print(name.strip())

file.close()
