print("Welcome to Guess the Number!")
print("The rules are simple. I will think of a number, and you will try to guess it.")
import random
number = random.randint(1,10)
isGuessRight = False
while isGuessRight != True:
    guess = input("Guess a number between 1 and 10: ")
    if int(guess) == number:
        print("You guessed {}. That is correct! You win!".format(guess))
        isGuessRight = True
    else:
        print("You guessed {}. Sorry, that isn’t it. Try again.".format(guess))
# Pseudocode:
# If the user has not guessed the correct answer, enter the loop.
# Ask the user for a guess.
# Check whether the guess is the correct number.
# If correct, tell the user and exit the loop.
# If incorrect, tell the user and continue the loop.
print("Count to 10!")
for x in range (0, 11):
    print(x)