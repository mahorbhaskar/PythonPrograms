'''
Guessing Game Challenge - Solution
Let's use while loops to create a guessing game.

The Challenge:

Write a program that picks a random integer from 1 to 100, and has players guess the number. The rules are:

If a player's guess is less than 1 or greater than 100, say "OUT OF BOUNDS"
On a player's first turn, if their guess is
within 10 of the number, return "WARM!"
further than 10 away from the number, return "COLD!"
On all subsequent turns, if a guess is
closer to the number than the previous guess return "WARMER!"
farther from the number than the previous guess, return "COLDER!"
When the player's guess equals the number, tell them they've guessed correctly and how many guesses it took!
'''

import random

num = random.randint(1, 100)

print("Welcome to Guess Me!")
print("I'm thinking of a number between 1 to 100.")
print("If Your guess is withing 10 of my number, I'll say you're Cold.")
print("If Your guess is more than 10 away from my number, I'll say you're Warm.")
print("If your guess is farther than your most recent guess I'll say You're getting Colder.")
print("If your guess is closer than your most recent guess, I'll say you're getting Warmer.")
print("Let's Play")
