#  Pythin has only 2 loops...
# for and while...


# condition = True
# while condition == True:
#     print("Condition is True") # Infinite Loop...
#     # to stop it after first iteration...
#     # condition = False
#     break

# count = 0
# while count < 10:
#     print("The condition is True")
#     # count = count + 1
#     count += 1

# print("After the loop")

# items = [1,2,3,4]
# for item in items:
#     print(item)

# for item in range(15):
#     print(item)
    # range function prints a string...

# To get index we can use ENUMERRATE :---
# items = [1,2,3,4]
# for item in enumerate(items):
#     print(item)

# items = ["Quincy", "Syd", "Beau"]
# for index, item in enumerate(items):
#     print(index, item) 

items = [1,2,3,4]
for item in items:
    if item == 2:
        continue
    print(item)

