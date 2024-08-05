weight=int(input('Enter your weight? '))
unit=input(f'(L)bs or(K)g ')

if unit.upper()=='L':
  print(f"You are {weight*.45} kilos")

else:
  print(f'Your are {weight/.45} lbs')
