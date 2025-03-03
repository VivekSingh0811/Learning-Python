# def hello(name, age):
#     print("Hello " + name)
#     print("Hello " + name + ", you are " + str(age) + " years old!")

# hello("Beau", 39)
# hello("Quincy", 15)





#  Sometimes what we change inside the functiuon dosen't reflect ourside the function...
# def change(value):
#     value = 2

# val = 1
# change(val)
# print(val)

# so in this function the value dosn't changes to 2 and remains 1...it's bcoz the the type of val is immutable...NOW see the function below..
# def change(value):
#     value["name"] = "Syd"

# val = {"name" : "beau"}
# change(val)
# print(val)
# Since dictionary is muttable, so we now the name will be updated...it will change from beau to syd after calling the cchange function...


# RETURN STATEMENTS :--- 
# A function can return a value using return statements...    

# def hello(name):
#     print("Hello " + name + "!")
#     return name

#  Using "return" is a commmon way to end a function if starting conditions are not met...
# def hello(name):
#     if not name:
#         return
#     print("Hello " + name + "!")
    
# hello(False) #This will return nothing...
# hello("beau")


#  We can "RETURN MULTIPLE VALUES" ...ny usin gcomma to seperate the return values...

# def hello(name):
#     print("Hello " + name + "!")
#     return name, "Beau", 8

# print(hello("Syd")) # apart from the print in hello finctio it's also gonna print the return statements...



#  SCOPE OF A VARIABLE...

# GLOBAL VARIABLE :---
# age = 8

# def test():
#     print(age)

# print(age)
# test()
# #  both will print 8...

# LOCAL VARIABLE :---
# def test():
#     age = 8
#     print(age)

# print(age) # so here it's not available outside the function, it is only available inside the function...
# test()



# NESTED FUNCTIONS :---

# def talk(phrase):
#     def say(word):
#         print(word)

#     words = phrase.split(' ') # split is a way to create a list out of string...
#     for word in words:
#         say(word)

# talk('I am going to buy milk')


# def count():
#     count = 0

#     def increment():
#         nonlocal count # top acccess the variable in inner function...we used nonlocal
#         count = count + 1
#         print(count)

#     increment()

# count()


#  CLOSURES :---So in this from the outer function  we return the nested function

def counter():
    count = 0

    def increment():
        nonlocal count
        count = count + 1
        return count
    
    return increment

increment = counter()
print(increment())
print(increment())
print(increment())
