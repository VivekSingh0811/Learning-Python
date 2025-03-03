# Sets are like tuples and unlike tuples they are muttable so we can change them...It may look like dictionary but it doesn't have keys...

set1 = {"Roger", "Syd"}
set2 = {"Roger"}

set3 = {"Roger", "Syd", "Roger"}
# A set can't have two or more similar items...
print(set3)

intersect = set1 & set2 # Inetrrsection
mod = set1 | set2 # Union
dif = set1 - set2 # difference between 2 sets

print(intersect)
print(list(intersect))
print(mod)
print(list(mod))
print(dif)

print("Roger" in set1)