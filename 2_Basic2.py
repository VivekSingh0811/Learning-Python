from enum import Enum


name = "Beau"
print(type(name))
print(type(name) == str)

print(isinstance(name, str))
# To check if the name is the instance if the string class...



age = 2
print(isinstance(age, int))
print(isinstance(age, float))

age = float(2)
print(isinstance(age, float))
# So we can change data type of any variable using the class constructor...

age = "20"
print(isinstance(age, str))
print(isinstance(age, int))

# age = int("20")
age = int(age)
print(isinstance(age, int))
print(age)



condition1 = True
condition2 = False

not condition1 #False
condition1 and condition2 #False
condition1 or condition2 #True



#OR OPERATOR :--
print(0 or 1)
print(False or 'hey')
print('hi' or 'hey') #first argument is not false so it's printed...
print([] or False) # first argument is False so second one is printed...
print(False or [])
# In python, in OR Operator...
# if the first argument is true, the second argument is ignored...
# And if first argument is false, the second is printed...
# Also in python OR, "[]" is considered as a False value...


#AND OPERATOR :--
print(0 and 1)
print(1 and 0)
print(False and 'hey')
print('hi' and 'hey')
print([] and False)
print(False and [])
# In python, in AND Operator...
# if first operator is true then only it evaluates second argument, if second is true, it returns second argument...
# So, if first argument is false it will return that argument...



# BITWISSE OPERATOR :--
# & binary AND
# | binary OR
# ^ binary XOR
# ~ binary NOT
# << shift left operation
# >> shift right operation

# is (Identity Operator): compares two objects and return true if both objects are same
# in (Membership Operator): checks if value is present in the list or any other simialr thing...


# TERNARY OPERATOR :--
def is_adult(age):
    if age > 18:
        return True
    else:
        return False
    
def is_adult2(age):
    return True if age > 18 else False
    #This is the Ternary Operator...

print(is_adult(21))
print(is_adult2(5))



# STRINGS :--
name = "Beau"
phrase = name + " is a good boy"
print(phrase)
name += " is a good boy"
print(name)


print("""Beau is 
      
39
      
years old""")


name = "Samosa"
print(name.lower()) # This returns a brand new string...
print(name) # This will remain in the upper case bcoz ...the upper one creates a brand new string and doesn't make any changes to original one...
print("mo" in name)

name = "Be\"au" #Escaping Character...
print(name)
print(name[2])



# BOOLEAN :--
# done = True
#done = False
# Numbers are always true except for the number zero...
done = 5 #it will be true even if we use negative values...
# done = 0

if done:
    print("Yes")
else:
    print("No")



# any : It checks if any of the element in the list is true...it returns true
# all : It checks if all of the element in the list are true...it returns true

# book_1_read = True
# book_2_read = False
# read_any_book = any[book_1_read, book_2_read]

# ingredients_purchased = True
# meal_cooked = False
# ready_to_serve = all[ingredients_purchased, meal_cooked]



# NUMBER DATA TYPES :--
num1 = 2+3j
num2 = complex(4,5)
print(num2.real, num2.imag)
print(num1.real, num1.imag)
#  In Python "j" is used to represent imaguinary part of a complex number...

print(round(5.495))
print(round(5.495, 1))



#  ENUM :--
#  these are used to create constants in python...once created then nobody can reassign the value...
# (from enum import Enum)

class State(Enum):
    INACTIVE = 0
    ACTIVE = 1

print(State.ACTIVE)
print(State(1))
print(State['ACTIVE'])

print(State.ACTIVE.value)
print(State['ACTIVE'].value)

print(list(State))
print(len(State))

