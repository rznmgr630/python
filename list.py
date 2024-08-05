numbers=[12,6,32,14,45,34,6,4,9,6,6,6,67,87]

print(numbers[0])
print(numbers[:])     # stars with index 0 to the end
print(numbers[4:])    # starts with index 4 to the last
print(numbers[-1])    # returns last element
numbers.append(10)    # add the element at the last position
# numbers.clear()     # to remove every elemets in the list
print(numbers.count(12)) # to count the no of occurance of 12
numbers.insert(0,13) # insert 13 at 0 index
numbers.remove(6) # to remove the first matched 6 from the list
numbers.pop() # remove the last items
# numbers.index(5) # get the index of first occurance of 5 (returns error if not found)
print(5 in numbers) # return true or false
numbers.sort() # sorts in ascending order
numbers.reverse() # after sort() will sort in descending order
newNumbers=numbers.copy() # create a new list but these 2 lists are independent to each other
print(f'After operations {numbers}')

print('======== FIND THE LARGEST NUMBER IN THE ABOVE LIST =========')
largest=numbers[0]
for number in numbers: 
  if number>largest:
    largest=number;

print(largest)

print('======== REMOVE DUPLICATE NUMBERS IN THE ABOVE LIST =========')
newList=[]
for number in numbers: 
  if not number in newList:
    newList.append(number);

print(newList)

# TWO DIMENSIONAL LISTS
print('========TWO DIMENSIONAL LISTS ==============')
datas=[
  [1,2,3],
  [4,5,6],
  [7,8,9]
]

for row in datas:
  for data in row:
    print(data)