# Basic Input & Output
# Print function
print('This string will be displayed in the outputs')
print('You can print \n escape characters too.')

# Input from a file
# Using Cotext Manager
with open('testwork.txt', 'w') as fileobj:
    fileobj.write('tomato\npasta\ngarlic')

with open('testwork.txt', 'r') as fileobj:
    lines = fileobj.readlines()

print(lines)

with open('testwork.txt', 'r') as fileobj:
    content = fileobj.read()
    line = content.split('\n')

print(line)

# Reading line by line
with open('testwork.txt', 'r') as fileobj:
    liness = []
    for linear in fileobj:
        liness.append(linear.strip())
        print(linear)


def raise_to_power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num
    return result


print(raise_to_power(int(input('What is the base number?')),
                     int(input('What is the power?'))))

with open('testwork.txt', 'a') as test:
    test.write('\nwelcome home gee')
try:
    with open('testwork.txt', 'r') as test:
        print(test.readlines())

except FileExistsError:
    print('File does not exist')


# Functions Examples
def square(x):
    return x * x


print(square(16))


def multiply(x, y=0):
    print('value of x=', x)
    print('value of y=', y)

    return x * y


print(multiply(y=3, x=13))
