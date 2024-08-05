guessCount=0
guessLimit=0
secretNumber=9

while guessCount<3:
  guess=input('Enter your guess ? ');
  if int(guess)==secretNumber:
    print('You win!')
    break;
  guessCount+=1

else:
  print('Sorry, You failed!')