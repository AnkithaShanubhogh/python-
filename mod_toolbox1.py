def square1(n):
    return n*n

def square2(list1):
    list2=[]
    len1=len(list1)
    for i in range(0,len1,1):
        temp=square1(list1[i])
        list2.append(temp)
    return list2

def cube1(n):
    return n*n*n

def cube2(list1):
    list2=[]
    len1=len(list1)
    for i in range(0,len1,1):
        temp=cube1(list1[i])
        list2.append(temp)
    return list2

def factorial1(n):
    fact1=n
    for i in range(n,2,-1):
        fact1=fact1*(i-1)
    return fact1

def factorial2(list1):
    list2=[]
    for i in range(0,3,1):
        temp=factorial1(list1[i])
        list2.append(temp)
    return list2

def factors(n):
    list2=[1]
    for i in range(2,n+1,1):
        div1=i
        if n%div1==0:
            list2.append(div1)
    return list2

def getPrimes(maxNumber):
    list1=[1,2,3]
    num1=4
    isPrime=True
    if num1%2==0:
        isPrime=False
            
    if isPrime==True:
        list1.append(num1)
        print(list1)

    for j in range(5,maxNumber,1):
        num1=j
        isPrime=True
        for i in range(2,j,1):
            if num1%i==0:
                isPrime=False
        if isPrime==True:
            list1.append(num1)
    return list1
