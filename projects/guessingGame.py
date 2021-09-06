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
First, pick a random integer from 1 to 100 using the random module and assign it to a variable
Note: random.randint(a,b) returns a random integer in range [a, b], including both end points.
'''
import random

num = random.randint(1,100)

print("WELCOME TO GUESS ME!")
print("I'm thinking of a number between 1 and 100")
print("If your guess is more than 10 away from my number, I'll tell you you're COLD")
print("If your guess is within 10 of my number, I'll tell you you're WARM")
print("If your guess is farther than your most recent guess, I'll say you're getting COLDER")
print("If your guess is closer than your most recent guess, I'll say you're getting WARMER")
print("LET'S PLAY!")

guesses = [0]

while True:
    guess = int(input("I'm thinking of a Number between 1 to 100.\nWhat is your Guess?"))

    if guess < 1 or guess > 100:
        print('Out of Bounds! Please Try Again..')
        continue
    # here we compare the guess to the number
    if guess == num:
        print(f'Congratulations,The number was {num}\nYou guessed it in only {len(guesses)} Guesses! ')
        break

    # If guess is incorrect then add guess to the List
    guesses.append(guess)

    # when testing the first guess, guesses[-2]==0 evaluates false
    # and bring us down to the second section section

    if guesses[-2]:
        if abs(num-guess) < abs(num-guesses[-2]):
            print('WARMER')
        else:
            print('COLDER')

    else:
        if abs(num-guess) <= 10:
            print('WARM!')
        else:
            print('COLD!')