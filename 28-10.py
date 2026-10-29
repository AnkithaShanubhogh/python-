'''exception handling --> A event that interupt flow of program  '''
# try-tests risky code
# except-handles an error 
# finally - always executes 
# raise - generates an exception manually

# """ Q1.ASK THE  USER TO ENTER THEIR AGE . IF THEY ENTER TEXT INSTEAD OF A NUMBER ,HANDLE THE ERROR."""
# try:
#   age=int(input("Enter your age:"))
# except ValueError:
#   print("Enter valid value!!")
# finally:
#   print("Clean up here")

# output: 
# 1, Enter your age:16
# Clean up here

# 2.Enter your age:jhsjhdxj
# Enter valid value!!
# Clean up here

# '''Q2.ASK THE USER FOR TWO NUMBERS AND DIVIDE THE FIRST BY THE SECOND .HANDLE DIVISION BY ZERO'''
# try:
#   a=int(input("Enter a number:"))
#   b=int(input("Enter a number:"))
#   res=a/b
# except ZeroDivisionError:
#   print("you cant divide by zero!!")
# finally:
#   print("clean up here!._.")

# # output:
# # Enter a number:15
# # Enter a number:0
# # you cant divide by zero!!
# # clean up here!._.

# '''Q3.ASK THE USER TO ENTER A NUMBER AND PRINT IT .IF THE INPUT IS INVALID ,PRINT INVALID INPUT'''
# try:
#   a=int(input("enter a number:"))
#   print(a)
# except ValueError:
#   print("input is Invalid")

# # 1.enter a number:sdfxsf
# # input is Invalid

# # 2.enter a number:45
# # 45


'''Q4.STARET WITH BALANCE=1000.ASK FOR A WITHDRAWAL AMOUNT.IF IT EXCEEDS THE BALANCE ,PRINT 'INSUFFICIENT BALANCE'''

try:
  amount=1000
  withdrawal_amount=int(input("Enter a amound to withdraw"))
  if amount>withdrawal_amount:
    print("Insufficient balance")
  bal=amount-withdrawal_amount
  print("balance amount is:",bal)
except Exception as e:
  print(e)


