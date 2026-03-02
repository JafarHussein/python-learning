# Lists-They hold multiple values, they are more like arrays.They hold data , the data they can be of different data types

users=['Dave','John', 'Sara']

data=['Dave', 42,True]

#Getting a specific Item from a list, when we know the position of the item in the list
print(users[0])

#Getting the value in the last position of the list
print(users[-1])

#Lists methods

#1. .index('string')->Returns the index of the provided string in a list
print(users.index('Dave'))

#2.[startingIndex:finishingIndex(not inclusive)]->The bracket notation returns a bunch of values exclusive of the finishing index
print(users[0:2])
#If you want all the data from the starting position to the finishing index, you just provide the staring index

#3. len()->Returns the length of the list
print(len(users))

#4. .append()->This adds data to the list at the ending position
users.append('Elsa')

#5. .extend()->This adds elements from an iterable like a list, tupel, string, set or a dictionary to the end of an existing list, modifying the original list in place
users.extend(['SpongeBob','Patrick', 'Squirdward','Sandy'])

#6. .insert()_>Adds an element to a specified position
# list.insert(index, element)

users.insert(0,'firstListElement')

#7. .remove('string')->Removes the stated string from the list
users.remove('Elsa')

#8. .pop()->removes an element from a list based on its index and returns the removed value
print(users)
print(users.pop())
print(users)

#9. del - deletes a particular element from a list
del users[0]
print(users)

#10 .clear()->Removes the elements of a list, leaving it empty without deleting the list itself
data.clear()
print(data)

#11. .sort()->Sorts the list in an alphabetical order
users.append('jimmy')
users.sort()
print(users)
#Note here the lowers case will always be the last element

users.sort(key=str.lower)
print(users)

nums=[1,2,3,4,5,6,7,8,9,10]
nums.reverse()
print(nums)

#sorting in reverse
nums.sort(reverse=True)
print(nums)

#Keepin the list the way it was but just sorting for a single instance
print(sorted(nums, reverse=False))

#Making a copy of the orginal list, then sorting

nums_copy=nums.copy()
my_nums=list(nums)
my_copy=nums[:]

#Tupels in Py

#Mutability:Lists are mutable, meaning you can modify, add, remove elements after creation, while
# Tupels are immuteable, meaning their contents cannot be changed once they are defined

my_tuple=tuple(('tuple_element_1','tuple_element_2','tuple_element_3'))
(one, *two, three)=my_tuple
print(one)
print(two)
print(three)

print(my_tuple.count(2))
#.count()->Returns the number of instances a particular element occurs
# Basically counting

