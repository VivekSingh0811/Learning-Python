# Generators are functions that return an object which can be iterated over ...They genrate only one object at a time and thus are more memeory efficient when dealing with large data set...

#  they hae "yield" kwyeord instead of "return" keyword...

# def my_gen():
#     yield 3
#     yield 1
#     yield 2

# g = my_gen()

# value = next(g) #it runs until it gets the yield statement...
# print(value) 

# # for next yield statement...bcoz now value = 1...so...
# value = next(g) #it runs until it gets the yield statement...
# print(value) 

# value = next(g) 
# print(value)

# # if we try to run for the d fourth time it will raise StopIteration...bcoz in generators object will always raise it, if it doesn't reach any yield statement...
# # value = next(g) 
# # print(value)

# We can also use generators to take input for some other funtions...
# print(sum(g))
# print(sorted(g)) # this will give a sorted LIST...



# ANOTHER EXAMPLE :---

# def countdown(num) :
#     print("Starting")
#     while num > 0:
#         yield num
#         num -= 1

# cd = countdown(4)
# # print(cd) this doesnt work directly here...the correct merthd is below...

# value = next(cd)
# print(value)
# print(next(cd))
# print(next(cd))
# print(next(cd))
# # print(next(cd)) 





# # ANOTHER EXAMPLE :--- (This will prove the advantage of generators that is how they are memory efficient...)


# import sys 

# def firstn(n):
#     nums = []
#     num = 0
#     while num < n:
#         nums.append(num)
#         num += 1
#     return nums

# # print(firstn(10))
# # print(sum(firstn(10)))
# # here we need a list to save all the nmbers...

# def firstn_generator(n):
#     num = 0
#     while num < n:
#         yield num
#         num += 1

# # print(sum(firstn_generator(10)))
# # So here we don't need a list to save all the nmbers...

# print(sys.getsizeof(firstn(100000)))
# print(sys.getsizeof(firstn_generator(100000)))
# # So clearly the sizer of generator object is less...



# Another Example :---

# def fibonacci(limit):
#     a, b = 0, 1
#     while a < limit:
#         yield a
#         a, b = b, a+b

# fib = fibonacci(30)

# for i in fib:
#     print(i)




# Generator Expresions :---

mygen = (i for i in range(10) if i%2 == 0)

for i in mygen:
    print(i)
# so here as well generator expression is much much smaller than list expression..