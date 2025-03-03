# This is Comment

my_message = "Hello World !!!"

my_message1 = 'Boby\'s World !!!'

my_message2 = "Boby's World !!!"

my_message3 = """Bobby's World was a
good cartoon in 1990s"""

print(my_message1)
print(my_message2)
print(my_message3)




# Length Function :---
print(len(my_message3))


#index:---
print(my_message[0])


#String Slicing:--
# my_message[starting_index:Ending _index+1]
print(my_message[0:5])
print(my_message[:5])
print(my_message[6:])




#String Methods:---

print(my_message.lower())
print(my_message.upper())

print(my_message.count('Hello')) #String Hello appears one time
print(my_message.count('l')) # letter 'l' appears 3 times

print(my_message.find('World')) # World starts at 6th index in our message
print(my_message.find('Universe')) # it returns -1 bcoz it cant find that string anywhere

print(my_message.replace('World','Universe')) #It returns a new string and doesn't make changes to original string

greeting = 'Hello'
name = 'Vivek'

message = greeting + name #combines without any spaces between them
print(message)
message = greeting + ', ' + name
print(message)

#String Formatting :---
message = '{}, {}. Welcome!!!'.format(greeting, name) # '{}' is called Placeholder
print(message)

# better way to do string formatting
message = f'{greeting}, {name}. Welcome!!!'
print(message)

message = f'{greeting}, {name.upper()}. Welcome!!!'
print(message)


# dir = this shows all the attributes and methods that we have used on that variable
print(dir(name))


# help() = tells us everything about it that is available for us
# but it cant be applied on name, it is applied on 'string' class

# print(help(str))
# print(help(str.lower))