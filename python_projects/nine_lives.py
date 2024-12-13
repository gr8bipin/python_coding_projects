# import the module

import random # random is imported to allow for the random selection of a secret word

# variables

lives = 9 # the player starts with nine lives 
            # lives represents the number of chances the player has to guess incorrectly (starts at 9)

words = ['pizza', 'fairy', 'teeth', 'shirt', 'otter', 'plane'] # Each item in the list is a string made up of five characters
                                                                # A list of potential secret words, each containing five characters

secret_word = random.choice(words) # this variable uses the random module's choice() function
                                    # randomly chosen word from the words list using random.choice()

clue = ['?', '?', '?', '?', '?'] # a list of placeholder characters (?) of the same length as the secret word, updated with correct guesses

heart_symbol = u'\u2764' # unicode character ♥ used to visually represent lives remaining

guessed_word_correctly = False # a boolean that tracks whether the player has guessed the word correctly

# function
# update_clue function updates the clue list with correctly guessed letters. It iterates through the secret_word and replaces the placeholder (?) with the guessed letter if it matches the current character in secret_word

def update_clue(guessed_letter, secret_word, clue): 
    index = 0 # initializes a variable index to zero. this will be used to track the position of each character in the secret_word during iteration
    while index < len(secret_word): # starts a while loop that runs until index reaches the length of the secret_word. this ensures that every character in the secret_word is checked
        if guessed_letter == secret_word[index]: # for each character in the secret_word, checks if the guessed_letter matches the character at the current position (index)
            clue[index] = guessed_letter # if a match is found, replaces the placeholder (?) at the same position (index) in the clue list with the correctly guessed letter
        index = index + 1 # increments index by 1 to move to the next character in the secret_word


# Game Logic

while lives > 0: # the game uses a while loop that runs as long as the player has lives left (lives > 0)
    print(clue) # clue is displayed to show the current state of the guessed word
    print('Lives left: ' + heart_symbol * lives) # the number of lives left is displayed using heart symbols
    guess = input('Guess a letter or the whole word: ') # the player inputs their guess (a letter or the whole word)

    if guess == secret_word: # if the player guesses the whole word correctly, the loop exits, and the player wins
        guessed_word_correctly = True
        break

    if guess in secret_word: # if the guess is a single letter and it is in the secret_word, the clue is updated using update_clue()
        update_clue(guess, secret_word, clue)
    else: # if the guess is incorrect, the player loses one life
        print("Incorrect. You lose a life.")
        lives = lives - 1

print("------------------------------------------------------------------------")
# Game End

if guessed_word_correctly: # if the player guesses the word (guessed_word_correctly becomes True), they win, and the secret word is revealed
    print('You won! The secret word was ' + secret_word)
else: # If the player runs out of lives, they lose, and the secret word is revealed
    print('You lost! The secret word was ' + secret_word)

print("------------------------------------------------------------------------")
print("------------------------------------------------------------------------")

# Example Gameplay

    # secret word: "pizza"
    # Initial clue: ['?', '?', '?', '?', '?']
    # Player guesses: 
        # First guess: p -> ['p', '?', '?', '?', '?']. 
        # Second guess: z -> ['p', '?', 'z', 'z', '?']. 
        # Third guess: pizza -> Player wins!

# Concepts demonstrated:
    # Lists: To hold the current state of the word being guessed (clue).
    # Loops: For repeatedly prompting the player for input until they win or lose.
    # Conditionals: To check the player's input against the secret word.
    # String manipulation: To update the clue and provide feedback.
    # User input: To make the game interactive.

# This code effectively demonstrates a basic structure for interactive games with feedback loops.