# abs() function
int_num = -25
float_num = -10.23
complex_num = (3+10j)

print('The absolute value of an integer number is',
      abs(int_num))
print('The absolute value of an float number is',
      abs(float_num))
print('The magnitude of an complex number is',
      abs(complex_num))

print(round(10.98013274702, 3))

# range((range(start,stop,step))
for i in range(3, 15, 2):
    print(i, end=' ', )

print('\n')


# Incrementing the values
for q in range(1, 144, 4):
    print(q, end=' ')

print('\n')

# Reverse Ranging (decrementing the values using negative step)
for s in range(123, 2, -3):
    print(s, end=' ')

print('\n')

# using for-loop with python range()
arr_list = ['MySql', 'MongoDB', 'PostgreSQL', 'Firebase']
for i in range(len(arr_list)):
    print(arr_list[i], end=' ')

# merging two range outputs
from itertools import chain

print('merging two range as one')
frange = chain(range(10), range(10,230,2))
for i in frange:
    print(i, end=' ')