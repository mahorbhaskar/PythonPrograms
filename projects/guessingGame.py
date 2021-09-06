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