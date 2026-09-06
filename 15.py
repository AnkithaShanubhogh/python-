class Complex:
    def__init__(self,real=0,img=0):
        self.real=real
        self.img=img
    def__add__(self,other):
        return Complex(self.real+other.real,self.img+other.img)
    def__str__(self):
        if self.img>=0:
            return "{}+i{}".format(self.real,self.img)
        else:
            return "{}-i{}".format(self.real,abs(self.img))
count=int(input("Enter how many numbers do you want to add:"))
complex_list=[]
for i in range(count):
    real_part=float(input(f"enter real part of complex number{i+1}:"))
    imag_part=float(input(f"enter imaginary part of complex number{i+1}:"))
    complex_list.append(Complex(real_part,imag_part))

sum_series=Complex()

for x in complex_list:
    sum_series += x

print("sum of given complex numbers is:",sum_series)
