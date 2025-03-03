#Once created cannot be modified...can't even add or remove items...

names = ("Roger", "Syd", "Beau")

print(names[0])
print(names[-1])

print(names.index("Roger"))

print(len(names))

print("Roger" in names)

print(names[0:2])

# Just like list, when we use sorted funtion in tuples, it creates a new tuple...
print(sorted(names))

newTuple = names + ("Tina", "Quincy") #We can create new tuples using existing tuples but we can never modify an existing tuple...
print(newTuple)



