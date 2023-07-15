# List Built-in functions
# len(list)
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(len(numbers))
# max(list)
print(max(numbers))
# min(list)
print(min(numbers))
# list.append(element)
numbers.append(10)
print(numbers)
# list.pop(index)
numbers.pop(2)
print(numbers)
# list.remove(number)
numbers.remove(10)
print(numbers)
# list.reverse()
numbers.reverse()
print(numbers)
numbers.reverse()
print(numbers)
# sum(list)
sum_of_numbers = sum(numbers)
print(sum_of_numbers)
# list.sort()
numbers.sort()
print(numbers)
numbers.sort(reverse=True)
print(numbers)
# list.index(element)
my_list = ['a', 'b', 'c', 'd']
b_index = my_list.index('b')
print(b_index)
# string sort
strings = ['cat', 'mammal', 'rats', 'antelope']
sort_by_alphabet = strings.sort()
sort_by_length = strings.sort(key=len)
print(sort_by_length)
print(sort_by_alphabet)

# List Comprehension
list_of_squares = []
for i in range(1, 10):
    square = i ** 2
    list_of_squares.append(square)

print(list_of_squares)


# Average of a list
# Printing average through a loop
def cal_average(num):
    sum_num = 0
    for t in num:
        sum_num = sum_num + t

    avg = sum_num / len(num)
    return avg


print('The average is', cal_average([13, 2, 23, 35, 67]))
# using sum() and len() built-in functions
number_list = [14, 312, 435, 656, 57, 87]
avg_of_numbers = sum(number_list) / len(number_list)
print('The average is', round(avg_of_numbers, 3))

# list count()
strings = ['cat', 'mammal', 'rats', 'antelope']
color_count = strings.count('mammal')
print('The count of color: green is', color_count)

# Removing Duplicates using Set
my_first_list = [1, 1, 3, 4, 4, 4, 6, 76, 8, 9, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
my_final_list = set(my_first_list)
print(list(my_final_list))
# Using temporary list
my_first_list = [1, 1, 3, 4, 4, 4, 6, 76, 8, 9, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print('List Before: ', my_first_list)
temp_list = []

for i in my_first_list:
    if i not in temp_list:
        temp_list.append(i)

my_first_list = temp_list
print('List after removing duplicates:', my_first_list)
# Using Dict
print('hello')
my_list_in_start = ['a', 'b', 'c', 'd', 'a', 'c', 'd']
my_final_list = dict.fromkeys(my_list_in_start)
print(list(my_final_list))
# using list comprehension
sequencess = [10, 2, 3, 5, 7, 9, 0, 7, 4, 11, 23]
final_Sequence = []
for n in sequencess:
    if n not in final_Sequence:
        final_Sequence.append(n)
sequencess = final_Sequence
print(final_Sequence)

