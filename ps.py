# Print your name dynamically using f string:

name = input("Enter your name : ")

print(f"Hello, {name}! Welcome to Python programming.")

# Find the index of double space in the given string:

name = " My name is Affnan  Sawad"

index_of_double_space = name.index("  ")
print(index_of_double_space)

index_of_S = name.find("S")
print(index_of_S)

replace_double_space_by_single_space = name.replace("  ", " ")
print(replace_double_space_by_single_space)

# Take 3 input of fruits and make a lists:

fruits = [ ]

f1 = input("Enter fruit 1 : ")
fruits.append(f1)

f2 = input("Enter fruit 2 : ")
fruits.append(f2)

f3 = input("Enter fruit 3 : ")
fruits.append(f3)

print(fruits)


# Count 0 in the given tupple

a = [1,2,3,4,0,0,0,0,5,6,7,8,9,0]

counting = a.count(0)
print(counting)

# Sum the list
a = [1,2,3,4,5,6,7,8,9]
print(sum(a))


x = {1,2,3,4,5,6,7,8,9,9,9,"a","a", "b"}

print(x)