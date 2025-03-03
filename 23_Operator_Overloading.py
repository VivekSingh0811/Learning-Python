
# class Dog:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

# roger = Dog("Roger", 9)
# syd = Dog("Syd", 7)
# How canwe compare ther above two objects of Dog class...for that we need operator overloading...


class Dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __gt__(self,other):
        return True if self.age > other.age else False

roger = Dog("Roger", 9)
syd = Dog("Syd", 7)

print(roger > syd)

# The __gt__ method is one of Python's "magic methods" (also called dunder methods), which allows customizing the behavior of comparison operators like  ">" ...

#Without defining __gt__, Python would raise a TypeError when trying to compare two Dog objects with > because Python does not inherently know how to compare custom objects...



# Execution Flow :--

# Define the Dog class with a custom __gt__ method
# Create two Dog objects: roger and syd
# Use the > operator, which calls roger.__gt__(syd)
# Inside __gt__, compare roger.age with syd.age
# Return True because roger.age (9) is greater than syd.age (7)
# Print the result: True
