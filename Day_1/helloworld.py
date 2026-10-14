# Day 1 - 30DaysOfPython

print(2+3)  # addition(+)
print(3-1)  # subtraction (-)
print(2*3) # multiplication (*)
print(3/2)  # division (/)
print(3**2) # exponential (**)
print(3//2) # floor division operator (//)

# Checking data types
print(type(10))     # Int
print(type(3.14))   # Float
print(type(1+3j))   # Complex number      
print(type('Cole')) # String
print(type([1, 2, 3]))  # List
print(type({'name':'Cole'}))    # Dictionary
print(type({9.8, 3.14, 2.7}))   # Set
print(type((9.8, 3.14, 2.7)))   # Tuple

# Euclidean distance exercise
print("The Euclidean Formula is: d = √((x2 - x1)² + (y2 - y1)²)")
print("Finding the distance between points (2, 3) and (10, 8)")
x1, y1 = 2, 3
x2, y2 = 10, 8
d = ((x2 - x1)**2 + (y2 - y1)**2)**0.5 # Exponential to the 1/2 power to find the square root
print("The distance between points (2, 3) and (10, 8) is:", d)