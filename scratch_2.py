num_rows = int(input('Enter the number of rows: '))
for i in range(1, num_rows + 1):
    for j in range(i):
        print('*', end=' ')
    print()

# Number Guessing Game
import random

number = random.randint(1, 50)
attempts = 0

while True:
    guess = int(input('Guess the number (between 1 to 50): '))
    attempts += 1

    if guess == number:
        print('Congratulations! You passed it correctly.')

    elif guess > number:
        print('Too High! Try again later')

    else:
        print('Too Low! Try again next time')

    if attempts >= 5:
        print('You have reached the maximum number of attempts, try again later! The number was', number)
        break




# Multiplication Generator
num = int(input('Enter a number: '))

for i in range(1, 23):
    print(num, 'x', i, '=', num * i)



# Age Calculator
birth_year = int(input('Enter your birth year: '))
age = 2023 - birth_year
print('Yor age is ', age)