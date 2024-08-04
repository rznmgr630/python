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