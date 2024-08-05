class Person:
  def __init__(self,name) -> None:
    self.name=name;

  def talk(self):
    print(f'{self.name} can talk' )


person1=Person('Rajan');
person1.talk();