try:
    result = 2/0

except ZeroDivisionError:
    print("Cannot divide by zero!")

finally:
    result = 1
# finally block ia always going to run...doesn't matter whether the code has catch error or not...

print(result) #1



#  We can create our own exceptions by using "raise Exception" :---

# raise Exception("An error!")

# But this raises a general exceptio..so berlow is the way to handle that...

try: 
    raise Exception("An Error !")

except Exception as error:
    print(error)




# We can also define our own exception class :---

class DogNotFoundException(Exception):
    """pass means nothing, so it does nothing"""
    print("Inside")
    pass

try:
    raise DogNotFoundException()

except DogNotFoundException:
    print("Dog not Found !")



# with statement is verey helpful to simplify working with exception handling...
#  for example...when we use with open we don't have to close the file...it closes automatically...

