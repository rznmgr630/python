def greetUser():
  print('Hello')
  print('Welcome to the team')

greetUser();


# ==============PARAMETER FUNCTIONS===================
# NOTE: If you want to use positional and keyword arguments you must have the positional argument at first
# and then the keyword argument

# postional arguments
def sum(a,b):
  print(f'The sum of {a} and {b} is {a+b}')

sum(12,14)

# keyword arguments
def calculateTotal(total,shipping,discount):
  print(total-(total+shipping)*discount)

calculateTotal(100,10,.1)

# ====================== RETURN FUNCTIONS =================

def square(value):
  return value*value;

result=square(12);
print(result)


# ====================== REUSABLE FUNCTION ==================
def emojiMapper(message):
  splittedMsg=message.split(' ');

  emoji_mapper={
    ':)':'😊',
    ':(':'😒'
  }

  output=''
  for msg in splittedMsg:
    output+=emoji_mapper.get(msg,msg);

  return output


msg=input('Enter your message? ')
print(emojiMapper(msg))