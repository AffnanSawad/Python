# Sets : contains values in { } . 
# dont contain duplicate values/
# immutable

x = {1,2,3,4,5,5,5, "Affnan"}
y = {5,6,7,8,9,10}

print(x)

x.add(200)
print(x)

x.remove(3)
print(x)

# clean()=> all values will be removed
# len()=> length
# pop()=> randomly remove hobe

print( x.union(y))
print(x.intersection(y))

# Empty set

s = set()
print(s)


# Dictionary : duplicate keys are not allowed

marks = {

    "Affnan" : 95,
    "Sawad" : 90,
    "Rafi": 100
}

print(marks)

print(marks["Affnan"])

print(marks.get("Sawad"))
print(marks.keys())
print(marks.values())
print(marks.update({"Rafi": 99}))
print(marks)