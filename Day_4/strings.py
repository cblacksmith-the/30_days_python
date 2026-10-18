# Day 4 of 30 Days of Python

# Exercises

# Concatenate the string 'Thirty', 'Days', 'Of', 'Python' into a single string
a, b, c, d = 'Thirty', 'Days', 'of', 'Python'
sentence = a + ' ' + b + ' ' + c + ' ' + d
print(sentence)

# Concatenate the string "Coding", "For", "All" into a single string
x, y, z = 'Coding', 'For', 'All'
statement = x + ' ' + y + ' ' + z
print(statement)

# Print the length of the statement
print(len(statement))

# Change all the characters in the statement to uppercase
print(statement.upper())

# Change all the characters in the statement to lowercase
print(statement.lower())

# Use capitalize(), title(), and swapcase() methods to format the value of the statement
print(statement.capitalize())
print(statement.title())
print(statement.swapcase())

# Cut (Slice) out the first word of the statement
print(statement[6:])

# Check if the statement contatins the word 'Coding' using the method index, find, or other methods
sub_string = 'Coding'
print(statement.index(sub_string)) # prints a 0, meaning 'Coding' is there, and it's location is starting at point 0 in the sentence
print(statement.find('Coding'))
print(statement.count('Coding')) # prints a count of 1, for one instance of 'Coding'

# Replace the word "Coding" in the string to "Python"
print(statement.replace('Coding','Python')) # only replaces 'Coding' for 'Python' within this print(), not throughout the script

# Change 'Coding for all' to 'Python for Everyone'
print(statement.replace('Coding For All', 'Python for Everyone'))

# Split the string 'Coding For All' using space as the separator
print(statement.split())

# "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma
print("Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon".split(', '))

# What is the character at index 0 in the string 'Coding For All'?
print(statement[0])

# What is the last index in the same string?
print(statement[-1])

# What character is at index 10 in the same string?
print(statement[10]) # None, because it's the space between 'For' and 'All'

# Create an acronym or abbreviation for the string 'Python For Everyone'
split_statement = 'Python For Everyone'.split() # breaking the string into a list
print(split_statement[0][0] + split_statement[1][0] + split_statement[2][0]) # the first [] is the word in the list, and the 2nd [] is the letter of that word

# Create an acronym or abbreviation for the string 'Coding For All'
acronym = statement.split()
print(acronym[0][0] + acronym[1][0] + acronym[2][0])

# Use index to determine the position of the first occurrence of C in Coding For All
print(statement.index('C'))

# Use index to determine the position of the first occurrence of F in Coding For All
print(statement.index('F'))

# Use rfind to determine the position of the last occurrence of l in Coding For All People
print((statement + ' People').rfind('l'))

# Use index or find to locate the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print('You cannot end a sentence with because because because is a conjunction'.find('because'))
print('You cannot end a sentence with because because because is a conjunction'.index('because'))

# Use rindex or find to locate the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print('You cannot end a sentence with because because because is a conjunction'.rindex('because'))

# Slice out the phrase 'because because because' in the previous string
bc_sentence = 'You cannot end a sentence with because because because is a conjunction'
bc_phrase = 'because because because'
bc_start = bc_sentence.find(bc_phrase)
bc_end = bc_start + len(bc_phrase)

print(bc_sentence[bc_start:bc_end]) # Variable-based slice
print('You cannot end a sentence with because because because is a conjunction'[31:54]) # hard-coded slice

# Does 'Coding For All' start with a substring 'Coding'?
print(statement.startswith('Coding'))

# Does 'Coding For All' end wit ha substring 'Coding'?
print(statement.endswith('Coding'))

# ' Coding For All ', Remove the left and right trailing spaces in the given string
print(' Coding For All '.strip(' '))

# Which one of the following variables return True when we use the method isidentifier():
print('30DaysOfPyton'.isidentifier()) # False
print('thirty_days_of_python'.isidentifier()) # True

# Join the following list of Python Libraries with a hash with a space string
pyth_libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print(' # '.join(pyth_libraries))

# Use the 'new line' escape sequence to separate the following sentences
    # I am enjoing this challenge.
    # I just wonder what is next.
print('I am enjoying this challenge. \nI just wonder what is next.')

# Use the 'tab escape' sequence to write the following lines:
    # Name  Age  Country    City
    # Phoebe 250 Finland    Helsinki
print('Name \tAge \tCountry \tCity \nPhoebe \t250 \tFinland \tHelsinki')

# Use the string formatting method to display the following:
    # radius = 10
    # area = 3.14 * radius ** 2
    # The area of the circle with radius 10 is 314 meters square
radius = 10
area = 3.14 * radius ** 2
print('The area of the circle with radius {} is {} meters square'.format(radius, area))

# Using the string formatting methods, perform arithmetic with two variable integers
a = 8
b = 6

print('{} + {} = {}'.format(a, b, a + b))
print('{} - {} = {}'.format(a, b, a - b))
print('{} * {} = {}'.format(a, b, a * b))
print('{} / {} = {:.2f}'.format(a, b, a / b))
print('{} % {} = {}'.format(a, b, a % b))
print('{} // {} = {}'.format(a, b, a // b))
print('{} ** {} = {}'.format(a, b, a ** b))

