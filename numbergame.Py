# Number Guessing Game
import random

number = random.randint(1, 100)
attempts = 0

while True:
    guess = int(input("Guess the number (between 1 and 100): "))
    attempts += 1

    if guess == number:
        print("Congratulations! You guessed it correctly.")
        break
    elif guess < number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")

    if attempts >= 5:
        print("You have reached the maximum number of attempts. The number was", number)
        break
