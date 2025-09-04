# 1
name = str( input("Enter your name : "))
age = int( input("Enter your age : "))

print(f"My name is {name} and i am {age} years old.")

# 2
number1 = int(input("Enter number 1 : "))
number2 = int(input("Enter number 2 : "))

division = number1 / number2
print( "Division is : ", division)

print( type(division))

# 3

num1 = str( input("Enter number 1 : "))

final_num = int(num1)

square_it = final_num ** 2

print("Square is : ", square_it)

# 4

name = str( input("Enter name : "))

print( name[0])
print( name[-1])
print( name.count("a"))
print( name.count("n"))

# 5

fruit = [ "banana", "apple", "mango", "orange"]

print( fruit[1])
print( fruit[-1])

# 6

numss = [1,2,3,4,5,6,7,8,9,10]

summation = sum(numss)
print(summation)

# 12
maximum = max(numss)
minimum = min(numss)
print(maximum)
print(minimum)
# 10

student = {

    "name": "Affnan",
    "age" : 20,
    "grade" : "A+",
}
print( student.values()) 
print( student["name"])
print(student["grade"])


# 13

num = { 1,2,3,4,5,5}

user = int( input("Enter a number : "))

if user in num:
    print("Present")

else:
    print("Not Present")

# 15
x = {1,2,3,4,5,6,7,8,9,9,9,"a","a", "b"}

print(x)

# 18
d1 = {"a": 1, "b": 2}
d2 = {"c": 3, "d": 4}

# how to merge two dictionaries
d1.update(d2)
print(d1)

