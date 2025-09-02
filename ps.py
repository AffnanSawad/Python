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