score = 0 # set a variable with starting value 0

print("Guess the Animal!") # create a message to introduce the game to the player

def check_guess(guess, answer): # check if the player's guess matches the correct answer
    
    global score # score variable is a global variable, changes to the variable can be seen throughout the whole program
    still_guessing = True # this variable will hold one of only two values: True or False
    attempt = 0

    while still_guessing and attempt < 3: # while loop runs the check code three times or until the player gets the answer correct- whichever comes first.
        if guess.lower() == answer.lower(): # make sure each line of code has the correct indent
            print("Correct answer")
            score = score + 1
            still_guessing = False
        else: # the else variable asks the player to enter another answer if they get it wrong
            if attempt < 2:
                guess = input('Sorry wrong answer. Try again. ')
            attempt = attempt + 1 # add 1 to the number of guesses the player has had

    if attempt == 3:
        print("The correct answer is " + answer)
        
guess1 = input("Which bear lives at the North Pole? ") # Ask a question (user input)
check_guess(guess1, 'polar bear') # this code tells the function to use the player's guess as the first parameter and the phrase "polar bear" as the second parameter

guess2 = input("Which is the fastest land animal? ")
check_guess(guess2, 'cheetah')

guess3 = input("Which is the largest animal? ")
check_guess(guess3, 'blue whale')

print('Your score is ' + str(score))