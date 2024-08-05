def greetUser():
  print('Hello')
  print('Welcome to the team')

greetUser();


# ==============PARAMETER FUNCTIONS===================
# postional arguments
def sum(a,b):
  print(f'The sum of {a} and {b} is {a+b}')

sum(12,14)

# keyword arguments
def calculateTotal(total,shipping,discount):
  print(total-(total+shipping)*discount)

calculateTotal(100,10,.1)