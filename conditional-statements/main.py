# If statements

# In the if else statement clause, a particular condition is checked, if the condition evaluates to true,
# The if block is executed else , the else block is executedp

meaning=42

if meaning > 10:
    print('Meaning is greater than 10')
else:
    print('Meaning is not greater than 10')


#Data Types 

#1.String data type

# first_name='Dave'
# last_name='gray'

#Checking the data type of a string

# print(type(first_name))
# print(type(last_name))
# print(isinstance(first_name, str))

#String concatination

first_name="Spongebob"
last_name="SquarePants"

full_name= first_name + last_name
print(full_name)

#String casting to an integer

decade=str(1980)
print(type(decade), decade)

statement='I like rock music from the' + decade + 's'
print(statement)

#Escaping special characters
sentence=' I\'m a backend engineer, trying to master python \t'

#String methods

#1. .lower()->This returns a copy of the string, with all the characters transformed to lowercase
character1="SpongeBob SquarePants"
print(character1.lower())

#2. .upper()->This returns a copy of the string with all the 
character2="Patrick Star"
print(character2.upper())

#3. title()->This will capitalize every first letter of the words in a sentence, more like the capitalize property in css
full_sentence='hello my name is spongebob squarepants and i live in bikini bottom'
print(full_sentence.title())

# .replace(word_to_replaced, word_to_be_introduced)
# .len()-Returns the length of a particular string
# .strip()->This removes the whitespaces from a series of characters i.e string
# .lstrip()->This removes whitespaces on the left side
# .rstrip()->This removes whitespaces from the right side of a string






