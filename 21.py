import csv

def read_csv_to_dict(filename):
    with open(filename,"r",encoding='utf-8')as f:
        return list(csv.DictReader(f))

def summarize_column(data,column,opearation):
    values=[]
    for row in data:
        if row[column] !='':
            values.append(float(row[column]))
    if operation == 'max':
        return max(values)
    elif operation == 'min':
        return min(values)
    elif operation == 'average':
        return sum(values)/len(values)
print("---data summary geneartor---")
filename=input("enter the name of csv file:")
data=read_csv_to_dict(filename)

column=input("Enter the column name:")
operation=input("Choose an operation(min/max/average):").lower()
result=summarize_column(data,column,operation)
print(f"{operation.title()} of {column}:{result:.2f}")
    
