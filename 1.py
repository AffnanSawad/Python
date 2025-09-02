# How to print in Python
print("Hello World !") 

# install: pip install pyjokes
import pyjokes

create_joke = pyjokes.get_joke()
print(create_joke)

# Multiline prints using triple quotes
print("""This is a multiline print,
      using triple quotes.
      It can span multiple lines.""")

# Chapter 2: Variables and Data Types
a=10
b=20
c=a+b
print("The summation of a+b is =", c)

# Data types
x = 5               # integer
y = 3.14            # floating
name = "Alice"      # string
is_student = True   # boolean
z= None            # NoneType

# Operators 

xy= 3 
yz = 4
yz += 1 # Increment yz by 1

result = xy * yz
print("The result of xy * yz is =", result)

# Comparison operators : < , >, <=, >=, ==, != , !

a = 10 <= 20
print("Is 10 less than 20? ", a) # True

#  Type Detection & Type Conversion

x = "32.86"
print(type(x))

y = float(x) # Convert string to float
print(type(y))
print(y)

# taking input from user

a = input("Enter Number 1 : ")
b = input("Enter Number 2 : ")

print( "Input 1 : ", a)
print( "Input 2 : ", b)

a = int(a) # Convert to integer
b = int(b) # Convert to integer

c = a + b
print( "The summation of a and b is : ", c)

# Practice :

a = 2 
b =8

average = (a+b)/2
print(a+b)
print(a*b)
print(b%a)

print( " the average of a and b is : " , average), 


xy = input("Enter a number : ")
xy = int(xy)

print(type(xy))

# Power

a = 10 

square = a ** 2
power_four = a ** 4

print("10 to the power 2 is : ", square)
print("10 to the power 4 is : ", power_four)

# End of Chapter 1 and Chapter 2 ;

# Thanku ;
