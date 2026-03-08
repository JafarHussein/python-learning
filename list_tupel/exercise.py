# I'm going to do a few coding exercises on list and Tupels to cement my understanding on things

import math

#Task 1

#Create a list of 5 countries.

countries=['USA','Canada','Belgium','Argentina','Mexico']

#Print the first country
print(countries[0])

#Print the last country
print(countries[-1])

#Print the length of the list
print(len(countries))

#Add one more country
countries.append("Germany")

#Remove one country
countries.remove('Mexico')

print(countries)


#Task 2

#Create a list of numbers and do the following:

numbers=[1,3,5,76,8,9,10]

#Sort the list

numbers.sort()

print(numbers)

#Reverse the list

reversed_list=numbers.sort(reverse=True)

print(reversed_list)

#Print the largest number

largest_number=max(numbers)
print(largest_number)

#Print the smallest number

smallest_number=min(numbers)
print(smallest_number)

#Print the length of the list
length_numbers=len(numbers)
print(length_numbers)


#Task 3

student={
    "first_name":"SpongeBob",
    "last_name":"SquarePants",
    "age":"27",
    "course":"computer_science"
}

#Do this:

#Print the student's name

full_name=student['first_name'] + " " + student['last_name']

print(full_name)

#Add a new key called "grade"

student['grade']='A'

#Change the age

student['age']=30

#Print all keys

for key in student.keys():
    print(key)

#Print all values

for value in student.values():
    print(value)

#Task 4

#Create a dictionary of a phone book.

phone_book={
    'Alice':'0712345678',
    'Bob':'0787654321'
}

#Do this

#Add 2 new contacts

phone_book['Charity']='0723456798'

phone_book['Charles']='0798675412'

#Check if "Alice" exists

if 'Alice' in phone_book:
    print("Alice is present in the phone book")
else:
    print("The key Alice doesn't exist in the phone book")

#Remove one contact

phone_book.pop('Charity')

#Print all contacts using .items()

for key, value in phone_book.items():
    print(f"{key}: {value}")


#Task 5

#Combine lists and dictionaries.

students=[
    {"Name":"Alice","Grade":"A"},
    {"Name":"Bob","Grade":"B"},
    {"Name":"Charles","Grade":"C"},
    {"Name":"Dave","Grade":"D"}
]

print(students[0]['Name'])

print(students[2]['Grade'])

students.append({'Name':'Jimmy','Grade':'C'})

for student in students:
    for key in student.keys():
        print(key)
    print()

# Create a dictionary from a list of numbers, where the key is the number and the value is the square of the number

number_list=[1,2,3,4,5,6]

number_dictionary=dict()

for number in number_list:
    number_dictionary=number ** 2

print(number_dictionary)




