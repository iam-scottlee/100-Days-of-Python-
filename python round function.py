from collections import Counter
listsss = ['x', 'x', 'z', 'y', 'q', 'z', 'z', 'y']
print(Counter(listsss))

my_str = 'How are you doing over there and how is your family, the quick brown fox jumps over the lazy dog'
print(Counter(my_str))

# Initializing from an empty counter and updating counter afterwards
_count = Counter()
# Updating Counter with update() method
_count.update('Enough is enough, i think i am allergic to suckers')
print(_count)
# To access values from specific elements in the counter
for char in 'is':
    print('%s: %d' % (char, _count[char]))

# Deleting a variable
dict1 = {'x': 4, 'y': 16, 'z': 13}
del dict1['x']
print(Counter(dict1))

# Arithmetic Operations on Python Counter
counter1 = Counter({'x': 4, 'y': 16, 'z': 13})
counter2 = Counter({'x': -1, 'y': 6, 'z': 1})

# Addiction
counter3 = counter1 + counter2
# Subtraction
counter4 = counter1 - counter2
# Union
counter5 = counter1 | counter2
# Intersection
counter6 = counter1 & counter2
print(counter6, '\n', counter5, '\n', counter4, '\n', counter3)

# Methods available in python counter
# elements(), most_common(value), subtract(), update()
counter10 = Counter({'x': 4, 'y': 16, 'z': 13})
_elements = counter10.elements()
for a in _elements:
    print(a, end=' ')

print('\n')

common_element = counter10.most_common(3)
print(common_element)

counter1 = Counter({'x': 4, 'y': 16, 'z': 13})
counter2 = Counter({'x': -1, 'y': 6, 'z': 1})

counter1.subtract(counter2)
print(counter1)

counter1.update(counter2)
print(counter1)

# Reassigning Counts in Python
counter10 = Counter({'x': 4, 'y': 16, 'z': 13})
counter10['x'] = 23
print(counter10)

# Get and Set the count of Elements using Counter
print(counter10['y'])

# Enumerate() in Python
lists = ['x', 'x', 'z', 'y', 'q', 'z', 'z', 'y']
e_list = enumerate(lists)
e_list2 = enumerate(lists, 2)
print(list(e_list))
print(list(e_list2))

# time.sleep() function
import time

print('Today was a really bland day')
time.sleep(1.5)
print('This message will be printed after 12 secs')

# Delaying using function
nameInput = input('What is your name?')
print(nameInput)

def acceptRequest():
    print('How are you {0}?'.format(nameInput))
    time.sleep(1.5)

acceptRequest()
print('Function Execution Delayed')

my_message = "TheKingTrader"
for i in my_message:
    print(i, end=' ')
    time.sleep(0.5)

