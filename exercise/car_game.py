hasStarted=True
command=''

while command != 'quit':
  command=input('> ').lower()

  if command=='start':
    if hasStarted:
      print('Car has already started')
    else:
      hasStarted=True
      print('Cas is started')

  elif command=='stop':
    if not hasStarted:
      print('Car has already stopped')
    else:
      hasStarted=False
      print('Cas is stopped')

  elif command=='help':
    print("""
        start - to start the car
        stop - to stop the car
        quit - to terminate the program
        help - to get available options
    """)

  elif command=='quit':
    break;

  else: 
    print("Sorry, I don't understand that")