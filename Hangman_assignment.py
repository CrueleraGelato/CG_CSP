# CG, Hangman Assignmemnt 
import random 

#create a list of 10 words on a separate txt file 

#create anohter file holds win/loss count 

# Use split(",") on the context of words txt documnents to create your list of words 
with open('CG_CSP\CG_CSP\words.txt.', "r") as file: 
    content = file.split("word")
# Pull win and lose totals from the other txt file and save them as 2 separate variables 
with open('CG_CSP\CG_CSP\win_count.txt', "w") as win: 
    content = win.write() 
with open('CG_CSP\CG_CSP\loss_count.txt', "w") as loss: 
    content = loss.write() 
# build hangman game 

# save the correct word as a variable random.choice(name of your list)
word = content.random.choice(content)
# number of wrong guesses 
wrong_guesses = "0"
# what letters have been guessed 
letters_guessed = "0"


# Fuction to display the hangman (Needs number of wrong guesses)
"""  ____
    |    |
    |    0
    |   /|\\
    |   / \\
    |_______

"""

# Function to show letters and spaces(the correct word, letters that have been guessed)
for letter in word: 
    print("_")
# loop over the correct word 
    #variable for display word (starts at an empty string) 
    #check if letter has been guessed
        #then add that letter to the display word 
    # if they haven't guessed the letter 
        #add an underscore to the display word 
# return the finishes display word (outside of the loop)

# Main game loop (while true)
    # call the function to show hangman 
    # print my function call to show display 
    # create variable for guessed letter 
    # add letter to our guessed letters 
    # check if the letter is not in the word 
        # increase our incorrect guesses 
    # check if the display word is the same as the word 
        # tell them they won! 
        #increase win total 
        # ask if they want to play again 
            #reset our random word, reset wrong guess count
    # check to see if they lost (if they have 6 wrong guesses)
        #tell them they lost 
        # tell them what the word was 
        # increase the lodt count 
            # ask if they want to play again 
            #reset our random word, reset wrong guess count
