# Accepting arguments from command line...
# for this we will need sys module...


# import sys

# print(sys.argv)
# # python 12_CommandLineArguments.py beau 39
# # type above in terminal then hit enter...



# name = sys.argv[1]
# print("Hello " + name)
# # python 12_CommandLineArguments.py beau
# # type above in terminal then hit enter...


#  BUT THE ABOVE METHOD IS NOT VERY CONVIENIENT SO WE WILL USE ANOTHER LIBRARY

import argparse
parser = argparse.ArgumentParser(
    description = 'This Program prints the name of my dogs'
)

parser.add_argument('-c', '--color', metavar = 'color', required = True, help = 'the color to search for')

args = parser.parse_args()
print(args.color)
# python 12_CommandLineArguments.py -c red
# type above in terminal then hit enter...
# In this if we call the program wrong it will tell us what argumments it need...

