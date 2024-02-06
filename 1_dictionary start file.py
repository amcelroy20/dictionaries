import random

phonebook = {'Chris':'555−1111',
             'Katie':'555−2222',
             'Joanne':'555−3333'}

'''

print()
print('*****  start section 1 - print dictionary ********')
print()

print(phonebook)
print(len(phonebook))

mydictionary = {}  #this would create an empty dictionary

mydictionary = dict(m=8, n=9) #m and n are the keys, 8 and 9 are the values
print(mydictionary)


print()
print('*****  end section 1 ********')
print()





print()
print('*****  start section 2 - search dictionary ********')
print()

name = 'Chris'

if name in phonebook:
    print(f'Name: {name} Phone Number: {phonebook[name]}')
else:
    print(f'{name} is not in the phonebook')



print()
print('*****  end section 2 ********')
print()







print()
print('*****  start section 3 - edit/append dictionary ********')
print()


print(phonebook)

phonebook['Joe'] = '555-0123'
phonebook['Chris'] = '555-4444'

print(phonebook)


print()
print('*****  end section 3 ********')
print()






print()
print('*****  start section 4 - delete/remove from dictionary ********')
print()

print(phonebook)
del phonebook['Chris']
print(phonebook)


print()
print('*****  end section 4 ********')
print()


'''



print()
print('*****  start section 5 - iterate through keys, values, items ********')
print()


for key in phonebook:
    print(f'Name: {key} Phone Number: {phonebook[key]}')

for values in phonebook.values():
    print(values)



print()
print('*****  end section 5 ********')
print()


'''


print()
print('*****  start section 6 - using get and clear ********')
print()






print()
print('*****  end section 6 ********')
print()



print()
print('*****  start section 7 - using pop method ********')
print()






print()
print('*****  end section 7 ********')
print()



print()
print('*****  start section 8 - using popitem ********')
print()






print()
print('*****  end section 8 ********')
print()



print()
print('*****  start section 9 - using random and converting to list ********')
print()





print()
print('*****  end section 9 ********')
print()


'''





