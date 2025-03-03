#  Key & Value pairs

dog = {"Name" : "Roger", "age" : 9, "color" : "white"}

print(dog["Name"]) # in this method we cannot have a default value unlike the "get" methpod...
print(dog['Name'])


# Changing value of a key :--
dog["Name"] = "Syd"
print(dog)
# Another method to print value of dicitonary
# print(dog.get("color"))
# print(dog.get("language", "Hindi")) #if it cannot find language in dictionary, it will print Hindi...


#  Adding a new key-value pair :--
dog["Favourite food"] = "Meat"
print(dog)


# Deleting a key-valuye pair :--
del dog["color"]
print(dog)


# Popping from Dictionary :--
# print(dog.pop("Name"))
# print(dog)



# Removing last key-valyue pair of dictianrry :--
# print(dog.popitem())
# print(dog)


# Copying dictionary :--
dogCopy = dog.copy()
print(dogCopy)


print("color" in dog)


#  Printing Keys of Dictionary :--
print(dog.keys())
print(list(dog.keys()))


#  Printing values of Dictionary :--
print(dog.values())
print(list(dog.values()))


#  Length of dictionary :--
print(len(dog))




