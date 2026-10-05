# CG, Hangman Assignmemnt 
import random
import os 

# Use split(",") on the context of words txt document
# to create your list of words
with open('CG_CSP\CG_CSP\words.txt', "r") as file:
    content = file.read().split(",")
word = random.choice(content)
    
for letter in word: 
    ord(letter) 
 
# Pull win and lose totals from the other txt files
with open('CG_CSP\CG_CSP\win_count.txt', "r") as win:
    win_count = (win.read())

with open('CG_CSP\CG_CSP\loss_count.txt', "r") as loss:
    loss_count = (loss.read())


# Save the correct word as a variable


# Number of wrong guesses
wrong_guesses = 0
letter_in_word = len(word)
# What letters have been guessed
guessed_letters = []
def count_total_letters(word):
    len(word)
if letter_in_word <= 





# Function to display the hangman
def show_hangman(wrong_guesses):

    if wrong_guesses == 0:
        print("""  ____
    |    |
    |
    |
    |
    |_______
    """)

    elif wrong_guesses == 1:
        print("""  ____
    |    |
    |    O
    |
    |
    |_______
    """)

    elif wrong_guesses == 2:
        print("""  ____
    |    |
    |    O
    |    |
    |
    |_______
    """)

    elif wrong_guesses == 3:
        print("""  ____
    |    |
    |    O
    |   /|
    |
    |_______
    """)

    elif wrong_guesses == 4:
        print("""  ____
    |    |
    |    O
    |   /|\\
    |
    |_______
    """)

    elif wrong_guesses == 5:
        print("""  ____
    |    |
    |    O
    |   /|\\
    |   /
    |_______
    """)

    elif wrong_guesses == 6:
        print("""  ____
    |    |
    |    O
    |   /|\\
    |   / \\
    |_______
    """)
        
# Function to show letters and spaces
def show_word(word, guessed_letters):

    display_word = "_"

    # Loop over the correct word
    for letter in word:

        # Check if letter has been guessed
        if letter in guessed_letters:
            display_word += letter

        # If they haven't guessed the letter
        else:
            display_word += "_"

    return display_word


# Main game loop
while True:

    # Pick a new random word
    word = random.choice(word)

    # Reset wrong guesses
    wrong_guesses = 0

    # Reset guessed letters
    guessed_letters = []

    # Game loop
    while True:

        # Show hangman
        show_hangman(wrong_guesses)

        # Show the word
        display_word = show_word(word, guessed_letters)

        print("Word:", display_word)
        print("Guessed letters:", guessed_letters)

        # Ask the player for a letter
        guessed_letter = input("Guess a letter: ").lower()

        # Make sure the player entered one letter
        if len(guessed_letter) != 1 or not guessed_letter.isalpha():
            print("Please enter one letter.")
            continue

        # Check if the letter was already guessed
        if guessed_letter in guessed_letters:
            print("You already guessed that letter!")
            continue

        # Add letter to guessed letters
        guessed_letters.append(guessed_letter)

        # Check if the letter is not in the word
        if guessed_letter not in word:
            wrong_guesses += 1
            print("Wrong guess!")

        else:
            print("Correct guess!")

        # Check if the display word is the same as the word
        display_word = show_word(word, guessed_letters)

        if display_word == word:

            print("\nYou won!")
            print("The word was:", word)

            # Increase win total
            win_count += 1

            # Save win count
            with open('CG_CSP\CG_CSP\win_count.txt', "w") as win:
                win.write(str(win_count))

            break

        # Check if they lost
        if wrong_guesses == 6:

            show_hangman(wrong_guesses)

            print("\nYou lost!")
            print("The word was:", word)

            # Increase loss total
            loss_count += 1

            # Save loss count
            with open('CG_CSP\CG_CSP\loss_count.txt', "w") as loss:
                loss.write(str(loss_count))

            break

    # Ask if they want to play again
    play_again = input("\nDo you want to play again? (y/n): ").lower()

    if play_again != "y":
        print("\nThanks for playing!")
        print("Wins:", win_count)
        print("Losses:", loss_count)
        break
