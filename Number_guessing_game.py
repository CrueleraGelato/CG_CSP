# CG, Number Guessing Game
the_number = 79

print("I am thinking of a number between 1 and 100. You have 6 tries to get it") 

Guess2 = int(input("What is your second Guess?"))

Guess3 =  int(input("What is your third Guess?"))

Guess4 =  int(input("What is your fourth Guess?"))

Guess5 =  int(input("What is your five Guess?"))

Guess6 =  int(input("What is your six Guess?"))

while True: 
    Guess1 = int(input("What is your first Guess?"))
    if Guess1 > the_number: 
        print("Too High!") 
    elif Guess1 < the_number: 
