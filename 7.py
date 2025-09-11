# Functions:

def average():

    number1 = int(input("Enter number 1 : "))
    number2 = int(input("Enter number 2 : "))

    average = (number1 + number2) / 2
    print( "Average is : ", average)

average()
print("End of program")

average()
print("End of program")


# Grretings

def greet():
    name = str( input("Enter name : "))
    
    print(f"Hello, {name} AssalamuAlaikum !")

greet()
print("End of program")    

greet()
print("End of program")



#  With parameters and arguments

def summation(a,b,c):

    sum_total = a + b + c
    print("Sum is : ", sum_total)


summation(10,20,30)
print("End of program")

summation(100,200,300)
print("End of program")


# Return 

def multiply(x,y):

    multiply_total = x * y

    return multiply_total

result = multiply(10,20)
print("Result is : ", result)


# Default parameters

def sum(a=10, b=20):

    sum_total = a + b
    print("Sum is : ", sum_total)


sum()
print("End of program")

sum(100,200)
print("End of program")


# Recurssion : factorial of a number

def factorial(n):

    if(   n==0 or n==1):
        return 1
    
    return n * factorial(n-1)

n = int(input("Enter number : "))
print(f"Factorial is : ", { factorial(n)})


# Recursion : sum of n natural numbers
def sum_n(n):
      if n == 0:   # base case
        return 0
      else:
        return n + sum_n(n - 1)

n = int(input("Enter number : "))
print(f"Sum is : ", { sum_n(n)})


# fibonacci

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    
n = int(input("Enter number : "))
print(f"Fibonacci is : ", { fibonacci(n)})