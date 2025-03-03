list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# Positive indexing : 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
# Negatuve Indexing : -10, -9, -8, -7, -6, -5, -4, -3, -2, -1

# list[start:end:step]  (end = index+1)

print(list)
print(list[:])
print(list[1:]) #It will print till end
print(list[:-1]) # This will print only till 8
print(list[0])
print(list[5])
print(list[-1])
print(list[0:6])
print(list[3:8])
print(list[-7:-2])
print(list[2:-1:2])
print(list[2:-1:-1]) # bcoz it can't go to 2 to 8 through negative step
print(list[-1:2:-1]) # here also it will go only till 3 bcoz in reverse...(end = index+1)

# we can use positive and negative indexing at the same time
print(list[1:-2])


                                                                                                                                           






sample_url = 'http://something.com'
print(sample_url)

# reverse the url
print(sample_url[::-1])

# Get the top level domain
print(sample_url[-4:])

# Print the url without the http://
print(sample_url[7:])

# Print the url without the http:// and the top level domain
print(sample_url[7:-4])


# Watch Later : String formatting video...link in description of 2nd video