# It is a way to create list in avery concise way...

numbers = [1, 2, 3, 4, 5]


# Using for loop :---
# numbers_power_2 = []
# for n in numbers:
#     numbers_power_2.append(n**2)


# Using lambda function :---
# numbers_power_2 = list(map(lambda n : n**2, numbers))


# Using LIST COMPRESSION :---
numbers_power_2 = [n**2 for n in numbers]



print(numbers_power_2)

