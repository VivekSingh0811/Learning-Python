#  Everything in python is object...
#  Objects has attributes and methods that can be accessed using the doc syntax...

age = 8
# age has the access to all properties and methods defined for the int objects...

print(age.real)
print(age.imag)
print(age.bit_length())


#  Methods available to an object depends on the type of the value...
items = [1, 2]
items.append(3)
items.pop()
print(id(items))

# We have discussed some objects are muttable and some are immutable...That depends on the items itself...if item provides method to change its contents then its muttable, otherwise its immutable...