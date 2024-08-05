for item in 'Python':
  print(item)

for item in ['Rajan','Hari']:
  print(item)

# for item in range(10): (return range from 0 to 9) 
# for item in range(5,10): (return range from 5 to 9)
for item in range(5,10,2): #(return number from 5 to 9 and step is 2)
  print(item)

total=0;
for price in [1,2,3,4,5,6,7,8,9]:
  total+=price;

print(f'Total is ${total}')

# generate coordinates
for i in range(4):
  for j in range(3):
    print(f'({i},{j})')