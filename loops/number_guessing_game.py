""""" 
    Number guessing game.
    
    We need the following:
    1. Random number within a particular range
    2. Capture guess from user
    3. Evaluate/check user guess against our random number
        - if correct - state the end of the game
        - if too high - notify user it's too high
        - if too low - notify user it's too low
    4. Notification messages to user of what is happening at each stage in our command line game
    
    * we will use a while loop, which will need a boolean argument of true to begin executing
    
"""""
import random

game_random_number = random.randint(1, 100)
#print(game_random_number)
game_active = True

while game_active:
    game_start_message = "Guess a number between 1 and 100"
    print(game_start_message)
    user_guess = int(input())  # casting user_guess string to an integer => wrapping it in int as we got error since in the if
    if user_guess == game_random_number:             # it can't compare a string to an integer, so we need to make the user_guess an int
        print("You guess correctly!")
        game_active = False   # --> close the while loop
    elif user_guess < game_random_number:
        print("Too low! Guess again!")
    else:
        print("Too high! Guess again!")







