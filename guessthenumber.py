#This is a guess the number game.
import random

print('Hello. What is your name?')
name = input()

print('Well, ' + name + ' I am thinking of a number between 1 to 20')
secretNumber = random.randint(1, 20)

for guessTaken in range (1, 7):
    print('Take a guess')
    guess = int(input())

    if guess < secretNumber:
        print('Your guess is too low.')
    elif guess > secretNumber:
        print('Your guess is too high.')
    else:
        break # This condition is for correct guess!
if guess == secretNumber:
    print('Good job ' + name + ' You guessed my number in ' + str(guessTaken) + ' guesses!')
else:
    print('Nope. The number I was thinking of was ' + secretNumber)