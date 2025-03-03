class Dog:
    def eat(self):
        print("Eating dog food")

class Cat:
    def eat(self):
        print("Eating cat food")

# here we have defined eat method in both the classes and we can call it regardless of the class it belongs to...

animal1 = Dog()
animal2 = Cat()

animal1.eat()
animal2.eat()
#  so here eat method doesn't have the exact same class but still it runs..so we have build a generalized interface and now we need not to know whether the animal is a cat or dog when we call eat on it...


