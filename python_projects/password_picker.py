# add the modules
import random
import string

# welcome the user
print("Welcome to Password Picker!")

# make an adjective list
adjectives = ['sleepy', 'slow', 'smelly', 'wet', 'fat', 'red', 'orange', 'yellow', 'green', 'blue', 'purple', 'fluffy', 'white', 'proud', 'brave']

nouns = ['apple', 'dinosaur', 'ball', 'toaster', 'goat', 'dragon', 'hammer', 'duck', 'panda']


adjective = random.choice(adjectives) 
noun = random.choice(nouns)
number = random.randrange(0, 100)
special_char = random.choice(string.punctuation)

password = adjective + noun + str(number) + special_char

print("Your new password is: %s" % password)

print("--------------------------------------------------------------------------------")

# Another one? 

print("Welcome to Password Picker!")

while True: # while loop starts here
    adjective = random.choice(adjectives)
    noun = random.choice(nouns)
    number = random.randrange(0, 100)
    special_char = random.choice(string.punctuation)

    password = adjective + noun + str(number) + special_char
    
    print('Your new password is: %s' % password)

    response = input('Would you like more passwords? Type y or n: ') # input() function asks the user to enter a response into the shell 

    if response == 'n': # if the answer is 'yes' (y), the loop returns to the start. If it's 'no' (n), the program exits the loop.
        break # the while loop ends here

print("--------------------------------------------------------------------------------")

print("--------------------------------------------------------------------------------")

# get multiple passwords

nouns = ['apple', 'dinosaur', 'ball', 'toaster', 'goat', 'dragon', 'hammer', 'duck', 'panda', 'telephone', 'banana', 'teacher'] # add few more words into nouns

colors = ['red', 'green', 'blue'] # add random color into each password to make it longer

while True:

    for num in range(3): # the for loop runs 3 times, and selects 3 different passwords
        
        adjective = random.choice(nouns)
        color = random.choice(colors)
        noun = random.choice(nouns)
        number = random.randrange(0, 100)
        special_char = random.choice(string.punctuation)

        password = adjective + color + noun + str(number) + special_char

        print("Your new password is: %s" % password)

    response = input("Would you like more passwords? Type y or n: ")

    if response == 'n': # if the answer is 'yes' (y), the loop returns to the start. If it's 'no' (n), the program exits the loop.
            break # the while loop ends here
