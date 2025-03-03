#  Decorators in python are a way to chamge or alter in anyway how a function works, decorators are defined with the at symbol followwed by the decorator name just before the function definition...

#  Decorator is a function that takes a function as a parameter, wraps the function in an inner function that performs the job it has to do and returns that inner function...

#  We use decorators when we want to change the behaviour of a function without modifying the function itself...r


def logtime(func):
    def wrapper():
        print("Before")
        val = func()
        print("After")
        return val
    return wrapper



@logtime
def hello():
    print("hello")

hello()


