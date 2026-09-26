# CG, Number Guessing Game
import random

# Secret number range: 1 to 100
# Player gets 6 attempts
secret_number = random.randint(1, 100)
max_attempts = 6

print("I'm thinking of a number between 1 and 100. You have 6 tries to guess it!")

guesses_used = 0

for guess_number in range(1, max_attempts + 1):
    guess = int(input("Guess #" + str(guess_number) + ": "))

    guesses_used += 1

    if guess > secret_number:
        print("Too high!")
    elif guess < secret_number:
        print("Too low!")
    else:
        print("Correct! You guessed it in " + str(guesses_used) + " tries!")
        break

else:
    print("You're out of guesses! The number was " + str(secret_number) + ".")