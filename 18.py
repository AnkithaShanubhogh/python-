print("\n---STUDENT GRADE TRACKER---")

def inputstudentdata():
    slist=[]
    n=int(input("enter number students:"))
    for i in range(n):
        print(f"student{i+1}")
        name=input("Enter name:")
        marks=float(input("Enter marks(out of 100):"))
        slist.append({'name':name , 'marks': marks})
    print("Student details are:",slist)
    return slist

def get_grade(marks):
    if marks >= 90:
        return 'A+'
    elif marks >= 80:
        return 'A'
    elif marks >= 70:
        return 'B'
    elif marks >=60:
        return 'C'
    elif marks >= 50:
        return 'D'
    else:
        return 'F'

def calculatesummary(students):
    if not students:
        print("No data available")
        return
    print("\n---summary report---")
    marklist =[ s['marks'] for s in students]
    print("Total students:",len(students))

    avg = sum(marklist)/len(marklist)
    print(f"Average marks = {avg}")

    Topper=max(students , key=lambda s:s['marks'])
    print("Topper is :",Topper['name'],":",Topper['marks'])

    lowest=min(students , key=lambda s:s['marks'])
    print("Lowest Scorer is:",lowest['name'],":",lowest['marks'])

    print("\n---GRADE SUMMARY---")
    for s in students:
        grade=get_grade(s['marks'])
        print(s['name'],"---",s['marks'],"---",grade)

students=inputstudentdata()
calculatesummary(students)

    
