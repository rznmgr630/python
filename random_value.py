import random

print(random.random())
print(random.random())
print(random.random())


print(random.randint(10,20)) # generate the value between 10 and 20
print(random.randint(10,20))
print(random.randint(10,20))
print(random.randint(10,20))
print(random.randint(10,20))
print(random.randint(10,20))


class Dice:
  def roll(self):
    first=random.randint(1,6)
    second=random.randint(1,6)
    return first,second


dice=Dice();
print(dice.roll())