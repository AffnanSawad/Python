# ### ✅ Final List (Problems Without `if` or `loop`)

# 1. Write a program that takes your **name** and **age** as input and prints:
#    `"Hello [name], you are [age] years old!"`.

# 2. Ask the user for two numbers and print their **sum, difference, product, and division**.

# 3. Convert a user’s input string into an **integer** and print its square.

# 4. Take a string as input and print its **first and last character**.

# 5. Store 5 of your favorite fruits in a **list** and print the **second and last fruit**.

# 6. Create a **list of numbers** from 1 to 10. Print the **sum of all numbers**.
#    *(No loop → just manually create the list and use `sum()`.)*

# 7. Write a program that stores student info in a **dictionary** like:

# ```python
# {"name": "John", "age": 20, "grade": "A"}
# ```

# Then print the student’s name and grade.

# 11. Take a sentence as input and print it in **reverse order**.
#     *(Using slicing, no loop needed.)*

# 12. Given a list of numbers, find the **maximum and minimum**.
#     *(Use `max()` and `min()` directly.)*

# 13. Write a program that merges two dictionaries:

# ```python
# d1 = {"a": 1, "b": 2}
# d2 = {"c": 3, "d": 4}
# ```

# 19. Create a dictionary where keys are numbers `1–5` and values are their **squares**. Example: `{1:1, 2:4, 3:9}`.
#     *(Manually write dictionary without loops.)*

# ---

# ### 📌 Total = **11 Problems**

# (these are solvable with your learned topics, without needing `if` or loops).

# ---


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


# Examples: { If , Elif , Else } related problems


# Given username are les than 10 characters or not

username = "Affnan Sawad"

if ( len(username)< 10):
    print("Username is less than 10 characters")

elif( len(username) == 10):
    print("Username is equal to 10 characters")

else:
    print("Username is greater than  10 characters")    


    #make a list of name and take a input name and check it is available in the list or not 

names = ["Affnan", "Sawad", "Rafi", "Sabbir", "Rasel"]

user = str( input("Enter a name : "))

if( user == "Affnan" or user == "Sawad" or user == "Rafi" or user == "Sabbir" or user == "Rasel"):

    print("Name is available in the list")

else:
    print("Name is not available in the list")   



# My name is available in the list or not
x = ["Affnan", "Sawad", "Rafi", "Sabbir", "Rasel"]   

myName = str( input("Enter a name : "))

if myName in x:
    print(f"{myName} is available in the list")

else:
    print( f"{myName} is not available in the list")    



    # Grading System
    #  80-100 => A+
    # 70-79 => A
    # 60-69 => A-
    # 40-59 => Pass
    # <40 => Fail

    marks = int( input("Enter your marks : "))

    if( marks  >=80 and marks <= 100):
        print("A+")

    elif( marks >= 70 and marks <= 80):
        print("A")    

    elif( marks >= 60 and marks <= 70):
        print("A-")

    elif( marks < 60 and marks >= 40):
        print("Pass")    

    else:
        print("fail")        

# Find out odd and even numbers

numbers = int( input("Enter a number : "))

if( numbers % 2 == 0):
    print("Even" , numbers)

else:
    print("Odd" , numbers)    



# Find out the greatest number among three numbers
input1 = int( input("Enter number 1 : "))    
input2 = int( input("Enter number 2 : "))
input3 = int( input("Enter number 3 : "))

if( input1 > input2 and input1 > input3):
    print("Input 1 is the greatest number")

elif( input2 > input1 and input2 > input3):
    print("Input 2 is the greatest number")

else:
    print("Input 3 is the greatest number")
