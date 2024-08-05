####################################### BASIC SYNTAX #############################################333 

# 1. ================ we can user single quote and double quote
name= 'Rajan Midun Magar'

print(name)

# first char
print(name[0]) 

# last char
print(name[-1])

# to get char from certain range 
print(name[0:4]) # it will exclude the char at index 4
print(name[0:]) # it will return all the char after index 0
print(name[:5]) # it will return all the char before index 5 but exclude 5
print(name[1:-1]) # it will return all the char from index 1 to the second last char(excluding the last char)

# 2. ================ to add multi line  we have to use ''' '''
mail=''' 
  Hi Rajan,
  Thank you for subscribing my channel.

  Sincerely
  Kaka

'''
print(mail)


################################## FORMATTED STRING ===============================================

firstName='Rajan';
lastName='Midun';

fullName=f'{firstName} {lastName}'
print(fullName)

################################## STRING METHODS ===============================================

course='Python for Beginners';

print(len(course)) # to get length of the string
print(course.upper()) # to convert the string to uppercase (it will not change the original string)
print(course.lower()) # to convert the string to lowercase (it will not change the original string)
print(course.title()) # to convert the first char of word in a string to upercase (it will not change the original string)
print(course.find('P')) # return the index of hte first matched char but if not matched will return -1 (it's case sensative)
print(course.replace('P','J')) # replace the matched char/word by the given word (if not found will return the original string)
print('Python' in course) # return boolean value if the given char/word exists
