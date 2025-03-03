# dict -> object
# list, tuple -> array
# str -> string
# int, long, float -> number
# True -> true
# False -> false
# None -> null

import json


# CONVERTING PYTHON DATA TRO JSON DATA :--- 

# person = {"name": "John", "age": 30, "city": "New York", "hasChildren": False, "titles": ["engineer", "programmer"]}

# personJSON = json.dumps(person, indent=4, separators=('; ', '= '), sort_keys=True) #this will dump our object as a json string

# print(personJSON)

# with open("person.json", "w") as file:
#     json.dump(person, file, indent=4) #This will create a person.json in our folder check it u will find it there....



# CONVERTING BACK JSON DATA TO PYTHON DATA :---

# person = '{"name": "John", "age": 30, "city": "New York", "hasChildren": False, "titles": ["engineer", "programmer"]}' #Note that this time the person is wrppwed in single quotes...

# personJSON = json.dumps(person, indent=4, separators=('; ', '= '), sort_keys=True) 
 
# person = json.loads(personJSON)
# print(person)

# print("\n")

# with open("person.json", "r") as file:
#     person = json.load(file)
#     print(person)






# ABOVE WE TOOK THE DICTIONARY NOW LETS SAY WE TAKE A CUSTOM USER CLASS :---

class User:

    def __init__(self, name, age):
        self.name = name
        self.age = age

user = User("Mark", 27)

def encode_user(o):
    if isinstance(o, User):
        return {"name": o.name, "age": o.age, o.__class__.__name__: True}
    else:
        raise TypeError("Object of type User is not JSON serializable")
    

from json import JSONEncoder

class UserEncoder(JSONEncoder):

    def default(self, o):
        if isinstance(o, User):
            return {"name": o.name, "age": o.age, o.__class__.__name__: True}
        return JSONEncoder.default(self,o)

# userJson = json.dumps(user, default=encode_user)
userJson = json.dumps(user, cls=UserEncoder)
print(userJson)

userJSON = UserEncoder().encode(user)
print(userJson) #This will give a string
print(type(userJson))



#  So the above was encodingour object...
#  Now we will decode it back...



user = json.loads(userJSON)
print(user) #This will give a dictionary
print(type(user))

# Since it's a dictionary and not a user object so we cannot call user.name...
# print(user.name)
# so to decode the user object we will write a custom decoding method...

def decode_user(dct):
    if User.__name__ in dct:
        return User(name=dct["name"], age=dct['age'])
    return dct

user = json.loads(userJSON, object_hook=decode_user)
print(user.name)