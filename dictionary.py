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


