samosa = [] #Empty List

dogs = ["Roger", 1, "Syd", True]

# Printing the list :--
print(dogs)
print(*dogs)
print(dogs[2])

# Changing values of list :--
dogs[2] = "Beau"
print(dogs[2])

# Appending in the list :--
dogs.append("Judah")
print(dogs)

# Inserting in the list :--
dogs.insert(2, "Test") #This will insert Test in index 2
print(dogs)

# Inserting Multiple items in the list using SLicing concept:--
dogs[1:1] = ["Test1", "Test2"]
print(dogs)
dogs[1:3] = ["samosa", "Chutney"] #selects the elements at index 1 (inclusive) up to index 3 (exclusive) in the dogs list and replaces by new elements
print(dogs)

#  Combinig two lists :--
dogs.extend(["Quincy", 5])
# dogs += ["Quincy", 5] #This is also a way to combine two lists...
print(dogs)


# Removing item from the list :--
dogs.remove("Quincy")
print(dogs)


# Popping element from the list :--
print(dogs.pop()) #This will remove & display last item of list 
print(dogs) 


# using membership operator in list :--
print("Roger" in dogs)


#Sorting the list :--
# It cannot sort if wee have int as wel as chars int the list..
items = ["Roger", "beau", "Beau", "Quincy"] 
items.sort()
print(items) 
# In sort method uppercase lettters are kept first then the lowercase ones...
# we can fix that, then it will sort according to the position of alphabets not caring about upper or lower case...
items.sort(key = str.lower)
print(items)
# sorting modifies the original list content so to avoid that first we can copy the list and hen make modifications...
itemscopy = items[::]
print(itemscopy) # this will give a list
# there is one more way to sort lists without madifying the original list...
list = ["amar", "Bhabha", "akbar", "anthony"]
print(sorted(list, key = str.lower))



# list expression :---
mylist = [i for i in range(10) if i%2 == 0]

for i in mylist:
    print(i)