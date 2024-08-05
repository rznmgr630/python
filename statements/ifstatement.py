isHot=False
isCold=False

if isHot:
  print('Its hot day today')
  print('Drink plenty of water');

elif isCold:
  print('Its cold day today')
  print('Wear warn clothers')

else:
  print('Its a lovely day')
  print('Have a gret day')


#2=================================  CALCULATE DOWN PAYMENT
amount=100000
hasGoodCredit=True
downPayment=0


if hasGoodCredit:
  downPayment=.1*amount;

else:
  downPayment=.2*amount

print(f'Down payment is ${downPayment}')