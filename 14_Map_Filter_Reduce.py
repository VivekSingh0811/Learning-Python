#  map() : used to run a functoin upon each item in an iteral item like a list and create a ew list with the same number of items but the values of each item can be changed...

# numbers = [1, 2, 3]

# def double(a):
#     return a*2

# when function is one liner, it's better to use lambda function
# double = lambda a : a*2

# result = map(double, numbers)

# Or we can directly write lambda function in the map...
# result = map(lambda a : a*2, numbers)

# print(list(result))





# filer() : It takes an iterable and returns a filter object which is another iterable but without some of the original items, so u can do so by returning "TRUE or FALSE" from the filtering function ...

# numbers = [1, 2, 3, 4, 5, 6, 7]

# def isEven(n):
#     return n%2 == 0

#  Here also we can use a lambda function, since the function is one liner...
# result = filter(lambda n : n%2==0, numbers)

# result = filter(isEven, numbers)

# print(list(result))




# reduce(): It is used to calculate a value of a sequence like a list...we need to import it from standard library
from functools import reduce

expenses = [('Dinner', 80), ('Car repair', 120)]

sum = 0

# for expense in expenses:
#     sum += expense[1]
# The above is the long way to do it...now wwe will use reduce

sum = reduce(lambda a, b : a[1] + b[1], expenses)


print(sum)