# Dictionary and Set Examples

#phoneBook = { 'Beatrice': '555-1111', 'Katie':'555-2222', 'Chris':'555-3333'}
#print(phoneBook)
#print(phoneBook['Katie'])
#if 'Chris' not in phoneBook:
#    print("No number available for Chris")
#else:
#    print(phoneBook['Chris'])

#Try adding to the dictionary
#phoneBook['Wilbur'] = '123-0987'
#phoneBook['Beatrice'] = '867-5309'
#print(phoneBook)

#Delete a value from the phonebook
#del phoneBook['Katie']
#print(phoneBook)

#Find number of elements in our dictionary
#numItems = len(phoneBook)
#print(numItems)

#Creating an empty dictionary
#phoneBook={}
#phoneBook['Chris'] = '555-1111'
#phoneBook['Shelby'] = '555-2222'
#print(" ")
#print(phoneBook)
#print(" ")

# For Loop
#for key in phoneBook:
#    print(key)

#Creating a Set
#mySet = set()
#mySet = set ('aabbcc')
#print(mySet)

#mySet = set (['one', 'two', 'three', 45])
#print(mySet)

#Can find the length of the set
#print(len(mySet))

#mySet.add(1)
#print(mySet)

#mySet.update([2,3,4])
#print(mySet)

#mySet.remove(1)
#print(mySet)

#mySet.discard(88)
#print(mySet)


#set1 = set ([1, 2, 3])
#set2 = set ([3, 4, 5])

#set3 = set1.union(set2)
#print (set3)

#set4 = set1.intersection(set2)
#print(set4)

#set5 = set2.difference(set1)
#print(set5)

#Symmetric Difference of Sets
#set1 = set ([1,2,3,4])
#set2 = set ([3,4,5,6])
#set3 = set1 - set2
#print(set3)

varTest = "Bill"
for char7 in varTest:
    print(char7.isupper())