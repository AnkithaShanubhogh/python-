def DivExp(a,b):
    assert a > 0,"AssertionError:'a'must be greater than zero"
    if b == 0:
        raise ZeroDivisionError("ZeroDivisionError:division by zero is not allowed")
    
    c=a/b
    return c
try:
    a=float(input("Enter number for a:"))
    b=float(input("Enter number for b:"))
    print("Result =",DivExp(a,b))

except AssertionError as x:
    print(x)
except ZeroDivisionError as x:
    print(x)
