# Day 2: 30 Days of Python Programming

# Level 1 Exercises: Declaring Variables

first_name = 'Phoebe' # a dog of mine
last_name = 'Blacksmith'
full_name = 'Phoebe Blacksmith'
country = 'United States'
city = "Seattle"
age = 6
year = 2026
is_married = False
is_animal = True
is_light_on = False
fur_color, weight, personality = 'cream', 60.7, 'frilly'

# Level 2 Exercises
## Check the data types of the variables declared above
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_animal))
print(type(is_light_on))
print(type(fur_color))
print(type(weight))
print(type(personality))

## Using the len() function to check the length of the first name
print('Character Length of First Name:', len(first_name))

## Compare the length of first name and last name
print('Length of First Name:', len(first_name))
print('Length of Last Name:', len(last_name))
print('Difference in Length:', len(last_name) - len(first_name))

## Declare 5 as num_one and 4 as num_two, then add them together and assign the value to a variable total
num_one = 5
num_two = 4
total = num_one + num_two
print('Sum of num_one and num_two:', total)

## Subtract num_two from num_one, and assign the value to a variable diff
diff = num_one - num_two
print('Difference of num_one and num_two:', diff)

## Multiply num_one and num_two, and assign the value to a variable product
product = num_one * num_two
print('Product of num_one and num_two:', product)

## Divide num_one by num_two, and assign the value to a variable division
division = num_one / num_two
print('Division of num_one by num_two:', division)

## Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
remainder = num_two % num_one
print('Remainder of num_two divided by num_one:', remainder)

## Calculate num_one to the power of num_two and assign the value to a variable variable_exp
variable_exp = num_one ** num_two
print('num_one raised to the power of num_two:', variable_exp)

## Find floor division of num_one by num_two and assign the value to a variable floor_division
floor_division = num_one // num_two
print('Floor division of num_one by num_two:', floor_division)

## Given the radius of a circle is 30 meters...

### Calculate the area of a circle an assign the value to a variable name of area_of_circle
import math
r = 30
area_of_circle = math.pi * (r ** 2)
print('The area of a circle with a radious of 30 meters is:', area_of_circle, 'Square Meters')

### Calculate the circumference of the circle and assign the value to the variable name of circum_of_circle
circum_of_circle = 2 * math.pi * r
print('The circumference of the circle is:', circum_of_circle, 'Meters')

### Take the radius as user input and calculate the area
input_area = float(input('Enter the radius of the circle:')) ** 2 * math.pi
print('The area of the circle is:', input_area, 'Square Meters')

## Use the built-in input function to get first name, last name, country, and age from a user and store the value to their corresponding variable names
input_first_name = input('What is your first name?')
input_last_name = input('What is your last name?')
input_country = input('What Country are you from?')
input_age = input('How old are you?')

print(f'Hi, my name is {input_first_name} {input_last_name}, and I am from {input_country}. I am {input_age} years old.')
