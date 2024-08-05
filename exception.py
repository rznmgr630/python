
try:
  age=int(input('Enter your age? '));
  print(age)
  risk=3000/age
  print(risk)

except ZeroDivisionError:
  print('Age cannot be zero.')
except ValueError:
  print('Invalid value.')