# Simple lambda function
adder = lambda x, y: x + y
print(adder(1, 2))


# Simple Function alternative
def adders(x, y):
    return x + y


print(adders(1, 2))

# Printing Strings in lambda
x = 'some kind of useless lambda function no one understands'
(lambda x: print(x))(x)


# Simple function alternative
def simpleString():
    print('Some kind of useless lambda function no one understands')
    return


simpleString()

# lambda in filter()
sequences = [10, 2, 3, 5, 7, 9, 0, 7, 4, 11, 23]
filtered_results = filter(lambda x: x > 3, sequences)
print(list(filtered_results))

# function in filter()
sequencess = [10, 2, 3, 5, 7, 9, 0, 7, 4, 11, 23]


def function(x):
    return x > 3


filtered_results = filter(function, sequencess)
print(list(filtered_results))

# lambda in map()
sequences = [10, 2, 3, 5, 7, 9, 0, 7, 4, 11, 23]
mapped_results = map(lambda x: x * x, sequences)
print(list(mapped_results))

# function for map()
sequences = [10, 2, 3, 5, 7, 9, 0, 7, 4, 11, 23]


def mapper(x):
    return x * x


functioned_mapper = map(mapper, sequences)
print(list(functioned_mapper))

# lambda in reduce()
from functools import reduce
sequences = [1, 2, 3, 4, 5, 6]
product = reduce(lambda x,y: x * y, sequences)
print(product)