info={
  'name':"Rajan Midun Magar",
  'age':27,
  'isActive':True
}

print(info)
print(info['name'])

info['name']='Kaka';
print(info['name'])
print(info.get('name1')) # returns the value and if not exists return None
print(info.get('name1','Hello')) # returns the value and if not exists return 'Hello'


#1. =======================EXERCISE 1 =====================
# takes the input from users as digit and map it with the words
input=input('Enter 4 digits> ');

digits_mapping={
  '1':'One',
  '2':'Two',
  '3':'Three',
  '4':'Four',
}
output=''
for num in input:
  output +=f' {digits_mapping.get(num,'!')}';

print(output)

