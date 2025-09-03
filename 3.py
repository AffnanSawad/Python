# List : is a container which contains different types of dataTypes

personal_info = [ "Affnan", 21, "Bangladesh", 3.75, True]

print(personal_info)

print( personal_info[0])
print( personal_info[0 : 5])

personal_info[0] = "Affnan Sawad"
print(personal_info)

personal_info.append("CSE")
print(personal_info)

personal_info.insert(3, "19-08-2004")
print(personal_info)

personal_info.pop()
print(personal_info)

personal_info.remove("19-08-2004")
print(personal_info)


# Example 2:
marks = [ 75, 85, 95, 80, 70]

marks.sort()

print(marks)


marks.reverse()
print(marks)


marks.append(100)
print(marks)

marks.pop()
print(marks)


marks.remove(70)
print(marks)
