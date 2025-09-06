# Loops => 1.for loop 2. while loop

i = 1 

while(i<6):
    print("Affnan Sawad")
    i = i + 1

   #Print the array elements using while loop
personal_infos = [ "Affnan", 21, "Student", "Bangladesh"]

i = 0 

while( i <len(personal_infos)) :
    print(personal_infos[i])
    i = i + 1




# For Loop : range(start, end, step)

for i in range(6):
    print( i )  # 0,1,2,3,4,5


    for i in range(1,6):
        print(i) # 1,2,3,4,5


        for i in range( 1, 11, 2):
               print( i ) 



personal_infos = [ "Affnan", 21, "Student", "Bangladesh"]


for info in personal_infos:
    print( info )


# 
A = [1,2,3,4,5,6,7,8,9,10]

for elemenets_of_A in A:
     
     if(  elemenets_of_A  % 2 == 0):
            print("Even Numbers Are: ", elemenets_of_A)
 
else:
  print("No even number")


# Multiplication Table
given_number = 5 
   
for i in range(1, 11):
        
        multiplication = given_number * i 
        print( multiplication )


# Greeting  the names in the list
names = [ "Affnan", "Sawad", "Arafat", "Rafsan", "Sabbir"]

for i in names :
     
     print( f"Hello, {i}  Assalamualaikum !")


# Table of 5 in Reverse Order
given_numbers = 5 

for i in range(10 ,0 , -1 ) :
     multiplication = given_numbers * i 
     print(" table of 5 in Reverse Order is :  ",multiplication )


    #  prime or not
n = int(input("Enter a number: "))

for i in range( 2 , n):
     if ( n % i == 0):
          print("Not a prime number")
          break

else:
     print("Prime Number")


        #   

list_of_nums = [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200] 


# Sum of all even numbers in the list
input_number = int(input("Enter a number : "))

summation = 0


for i in range( 1 , input_number):
     if( i % 2 == 0):
          
          summation = summation + i

print("The sum of all even numbers is : ", summation)
        



