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
digits=input('Enter 4 digits> ');

digits_mapping={
  '1':'One',
  '2':'Two',
  '3':'Three',
  '4':'Four',
}
output=''
for num in digits:
  output +=f' {digits_mapping.get(num,'!')}';

print(output)


#2. ==================== EXERCISE 2 ======================
# map characters emoji to actual emoji
msg=input('Enter your message? ')
splittedMsg=msg.split(' ');

emoji_mapper={
  ':)':'😊',
  ':(':'😒'
}

output1=''
for msg in splittedMsg:
  output1+=emoji_mapper.get(msg,msg);

print(output1)