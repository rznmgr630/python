class Person:
  def __init__(self,name) -> None:
    self.name=name;

  def talk(self):
    print(f'{self.name} can talk' )


person1=Person('Rajan');
person1.talk();

#=========================== INHERITANCE
class Animal:
  def walk(self):
    print('Can walk')


class Dog(Animal):
  pass;

class Cat(Animal):
  def eatMouse(self):
    print('Cat eats mouse')


dog=Dog();
dog.walk()

cat=Cat();
cat.walk()
cat.eatMouse()