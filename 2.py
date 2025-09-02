
# String 
# Different ways to declare string
name = "Affnan Sawad"
name = 'Affnan Sawad'
name = '''Affnan Sawad'''
name = """Affnan Sawad"""

# indexing of a string : [ start : end : skipping]

name = "Affnan Sawad"

indexing_string = name[ 0 : 12 ]
print(indexing_string)

# Reversing a string : 

reverse_the_string = name[ -1 : : -1]
print(reverse_the_string) 

# skip 2 characters
skipping = name[ 0 : 12 : 3]
print(skipping)   #An w

#  [ 0 : ] means start from 0 to end
#  [ : 12 ] means start from 0 to 12

# Funtions of string

name = "Affnan"

finding_length = ( len(name))
print(finding_length)

print(name.lower())
print(name.upper())
print(name.replace("A" , "Z"))
print(name.count("f"))
print(name.index("n"))
print(name.isalnum())
print(name.isalpha()) 
print(name.endswith("n")) 
print(name.startswith("A"))
print(name.capitalize()) 
print(name*3) 
print(name + " Sawad") 
print(name[0]) 

# To know more about string functions use ChatGpt