# type()
str_list = 'Welcome to TheKIngTrader Page'
age = 50
pi = 3.14
c_num = 3j + 10
my_list = ['a', 'b', 'c', 'd']
my_set = {'a', 'b', 'c', 'd'}
my_tuple = ('a', 'b', 'c', 'd')
my_dict = {'a': 'A', 'b': 'B', 'c': 'C', 'd': 'D'}

print('The type is:', type(str_list))
print('The type is:', type(age))
print('The type is:', type(pi))
print('The type is:', type(c_num))
print('The type is:', type(my_list))
print('The type is:', type(my_set))
print('The type is:', type(my_tuple))
print('The type is:', type(my_dict))


# Using type() for class object
class test:
    s = 'testing'


t = test()
print(type(t))


class MyClass:
    x = 'Hello world'
    y = 50


t1 = type('New Class', (MyClass,), dict(x='Hello World', y=50))
print(type(t1))
print(vars(t1))

# isinstance()
