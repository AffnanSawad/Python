# If - Else

a = int(input("Enter your age : "))

if(a>18):
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")

# Elif
a = int(input("Enter your age : "))

if(a>18):
    print("You are eligible to vote")

elif(a < 0):
    print("Invalid age")

elif(a == 0):
    print("You are not born yet")

elif( a == 18):
    print("You are just eligible to vote")   


else:
    print("You are not eligible to vote")


# Examples:
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