# 1.============================== ARITHMETIC OPERATORS ========================================== 
print('======== ARITHMETIC OPERATORS=======')
print(10+3)
print(10-3)
print(10*3)
print(10/3) #return floating point result
print(10 // 3) # return the integer result ignoring the value after .
print(10%3)

# 2.============================== ASSIGNMENT OPERATORS ========================================== 
print('======== ASSIGNMENT OPERATORS=======')
x=10
x+=3
x-=3
x*=3
x/=3
print(x)

# 2.============================== LOGICAL OPERATORS ========================================== 
print('======== LOGICAL OPERATORS=======')
hasHighIncome=True
hasGoodCreditScore=True
notCriminalRecord=True

# ========= AND OPERATOR
if hasHighIncome and hasGoodCreditScore:
  print('Eligible for loan')

else:
  print('Not eligible for loan')

# ========OR OPERATOR
if hasHighIncome or hasGoodCreditScore:
  print('Eligible for loan')

else:
  print('Not eligible for loan')

# ========== NOT OPERATOR
if hasHighIncome and not notCriminalRecord:
  print('Eligible for loan')

else:
  print('Not eligible for loan')