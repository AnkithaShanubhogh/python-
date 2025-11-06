x=float(input("what's x ?")) 
y=float(input("whats y ?"))
z=round(x+y)
print(f"{z:,}")                                           # comma as output                             

x=float(input("what's x ?")) 
y=float(input("whats y ?"))
z=round(x / y , 2 )
print(f"{z}")                                           # 2 decimal places as output roundfigures   

x=float(input("what's x ?")) 
y=float(input("whats y ?"))
z=round(x / y)
print(f"{z:.2f}")                                                # 2 decimal places as output roundfigures

x=float(input("what's x ?")) 
y=float(input("whats y ?"))
z=(x/y,2)
print(f"{z}")                                                      # tuple as output

x=float(input("what's x ?")) 
y=float(input("whats y ?"))
z=(x / y)
print(f"{z:.2f}")                                                   # 2 decimal places as output
