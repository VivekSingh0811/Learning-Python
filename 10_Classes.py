#  Class : it is a type of an object
#  Objecct : It is an instance of a class

# class Dog:
#     # Now we will write a method for a class ...
#     def bark(self):
#         print("woof!")

# Self : It is an argument of the method which will point to the current object instance..It must be specified when defining a method...So, when we defina a method inside a class , we will always start with self

# roger = Dog()
# print(type(roger))



# A special method called "init", which is a "CONSTRUCTOR"...
# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def bark(self):
#         print("woof!")

# roger = Dog("Roger", 9)
# print(roger.name)
# print(roger.age)
# roger.bark()


# Important Feature of Class :
# INHERITANCE :---

class Animal:
    def walk(self):
        print("Walking...")




class Dog(Animal): #now Dog class will Inheit from the Animal Class
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print("woof!")

roger = Dog("Roger", 9)
print(roger.name)
print(roger.age)
roger.bark()
roger.walk() #inheritance

