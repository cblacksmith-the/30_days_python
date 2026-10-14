# Day 3: Different Operators

## Example: Working with Declared Variables

### Declaring variables at the top

a = 3
b = 2

### Arithmetic operations while assigning the results to a variable

total = a + b
diff = a - b
product = a * b
division = a / b
remainder = a % b
floor_division = a // b
exponential = a ** b

print('a + b =', total)
print('a - b =', diff)
print('a * b =', product)
print('a / b =', division)
print('a % b =', remainder)
print('a // b =', floor_division)
print('a ** b = ', exponential)

## Excercises

### Declare your age, height, and a complex number as integer variables
age = int(67)
height = float(6 + 7/12) # :)
complex_num = 7j

print(type(age))
print(type(height))
print(type(complex_num))

### Write a script that prompts the user to enter the base and height of a triangle, then calculate the area of this triangle
tri_base = float(input('Enter the base of the triangle:'))
tri_height = float(input('Enter the height of the triangle:'))
tri_area = 0.5 * tri_base * tri_height
print(f'The area of the triangle is: {tri_area}')

### Write a script that prompts the user to enter each side of a triangle, then calculate the perimeter of this triangle
a = float(input('Enter side a:'))
b = float(input('Enter side b:'))
c = float(input('Enter side c:'))
perimeter = a + b + c

print(f'The perimeter of the triangle is: {perimeter}')

### Calculate the area and the perimeter of a rectangle using a prompt to find the length and width from the user
rec_length = float(input('Enter length:'))
rec_width = float(input('Enter the width'))
rec_area = rec_length * rec_width
rec_perimeter = (2*rec_width) + (2*rec_length)

print(f'The area of the rectangle is {rec_area} square meters, and the perimeter is {rec_perimeter}')

### Calculate the radius of circle using a prompt, then calculate the area and circumference
import math
circle_radius = float(input('Enter the radius of the circle:'))
circle_area = math.pi * circle_radius ** 2
circle_circumference = 2 * math.pi * circle_radius

print(f'The area of the circle is {circle_area} square meters, and its circumference is {circle_circumference}')

### Calculate the slope, x-intercept, and y-intercept of y = 2x - 2
m = 2
b = -2

y_int = m * 0 + b
x_int = -b / m

print('Slope:', m)
print('x intercept:', x_int)
print('y intercept:', y_int)

### Find the Slope and the Euclidean distance between point (2, 2) and point (6, 10)
xa, xb, ya, yb = 2, 6, 2, 10
slope = (yb - ya) / (xb - xa)

euc_distance = ((xb - xa) ** 2 + (yb - ya) ** 2) ** 0.5

print(f'The slope between these points is {slope}, and the Euclidean distance is {euc_distance}')

### Compare the last two slopes
print(m > slope)
print(m < slope)
print(m == slope)
print(m != slope)

### Calculate the value of y in (y= x^2 + 6x + 9)

x = -3
y = x ** 2 + 6 * x + 9

print(f'y = {y}')

### Find the length of 'python' and 'dragon' and make a falsy comparison statement
print(len('python'))
print(len('dragon'))
print(len('python') > len('dragon'))

### Use AND operator to check if 'on' is found in both 'python' and 'dragon'
print('on' in 'python' and 'on' in 'dragon')

### 'I hope this course is not full of jargon'. Use IN operator to check if jargon is in the sentence
print('jargon' in 'I hope this course is not full of jargon')

### Find the length of the text python and covert the value to float, and then to string
print(len('python'))
print(type(float(len('python'))))
print(type(str(len('python'))))

### Check if a number is even or odd
print(2 % 2 == 0, 9 % 2 == 0) # Dividing a odd number by 2 should leave a remainder of 1, and even a remainder of 0

### Check if the floor division of 7 by 3 is equal to the int converted value of 2.7
print(7 // 3 == 2.7) # Non-Integer converted value
print(7 // 3 == int(2.7))

### Check if type '10' is equal to type of 10
print(type('10') == type(10))

### Check if int('9.8') is equal to 10
print(int(float('9.8')) == 10) # False because int doesn't round

### Write a script that prompts the user to enter hours and rate per hour. Calculate the pay of the person
hours = float(input('How many hours do you work per week? '))
rate = float(input('How much do you make per hour? '))
week_earning = hours * rate
print(f'You make ${week_earning} each week')

### Write a script that prompts the user to enter how old they are, then calculate how many seconds that is
years = float(input('How old are you? '))
secs_lived = years * 365 * 24 * 60 * 60 
print(f'You have lived for {secs_lived} seconds.')

### Write a script that displays the following table:
# 1 1 1 1 1
# 2 1 2 4 8
# 3 1 3 9 27
# 4 1 4 16 64
# 5 1 5 25 125

row_a = [1, 1, 1, 1, 1]
row_b = [2, 1, 2, 4, 8]
row_c = [3, 1, 3, 9, 27]
row_d = [4, 1, 4, 16, 64]
row_e = [5, 1, 5, 25, 125]

print(row_a)
print(row_b)
print(row_c)
print(row_d)
print(row_e) # More or less prints a collection of lists... working on tables soon
