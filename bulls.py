"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Miroslav Babka
email: miroslav.babka@email.cz
discord: miro3363_98687
"""
import random
from sys import argv
from time import time
from os import system, name
# from time import strftime
# from time import gmtime

# Import messages (default EN and check if other language requsted)
if len(argv) > 1:
    if argv[1].upper() == 'CZ':
        import bulls_msg_cz as msg
    else:
        import bulls_msg_en as msg
else:
    import bulls_msg_en as msg

# Global variables
games_results = {}
next_play = bool(True)

# Functions
def clear_screen():
    """ Clear terminal screen - either unix or win """
    # for windows
    if name == 'nt':
        system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        system('clear')

def generate_secret_numbers(new_list):
    """ Generate 4 random digits - just leading zero is not allowed """
    # new_list = [0, 0, 0, 0]
    while new_list[0] == 0:
        new_list = random.sample([0,1,2,3,4,5,6,7,8,9], len(new_list))
    return new_list

def get_new_guess_from_user():
    """ Get new guess - 4 unique numbers , leading zero not allowed """
    print(msg.MSG_SEP_LINE)
    while True:
        new_guess = input(msg.MSG_INPUT).strip()
        # Test input leading zero, correct length and digits only
        if (new_guess[0] == '0') or (len(new_guess) != 4) or (not new_guess.isdigit()):
            print(msg.MSG_BAD_INPUT)
        # Test input for unique digits
        elif list(new_guess) != list({x:x for x in new_guess}.values()):
            print(msg.MSG_BAD_INPUT)
        else:
            break
    # Return new guess as list of integers (same format generated list is)
    return [int(x) for x in new_guess]

def evaluate_new_guess(guess, secret):
    """ Count cows and bulls for given set """
    sum_bulls, sum_cows = 0, 0
    for x in range(0, len(guess)):
        sum_bulls += 1 if guess[x] == secret[x] else 0
        sum_cows += 1 if guess[x] in secret and guess[x] != secret[x] else 0
    return bulls, cows

def results_of_the_round(sum_bulls, sum_cows, last_list, counter) -> bool:
    """ Print result and evaluate if next round necessary """
    print(f"{sum_bulls} {msg.MSG_BULLS[sum_bulls < 2]}, {cows} {msg.MSG_COWS[sum_cows < 2]}")
    if sum_bulls == len(last_list):
        # This game is over
        print(msg.MSG_FINAL_RESULT.format(counter))
        print(msg.MSG_SEP_LINE)
        # Print evaluation 1 - 4 amazing, 5 - 9 average, 10 - 14 not so good else bad
        final_result = counter // 5  if counter // 5 < 4 else 3
        print(msg.MSG_EVALUATION.format(msg.MSG_EVALUTION_GRADES[final_result]))
        # Print elapsed time
        elapsed_time = int(time() - start_time)
        print(msg.MSG_TIME_ELAPSED.format(elapsed_time))
        print(msg.MSG_SEP_LINE)
        # Save game result and print statistics
        games_results[len(games_results)] = [counter, elapsed_time]
        print(msg.MSG_GAME_SCORE)
        print(msg.MSG_SEP_LINE)
        for x in range(0, len(games_results)):
            print(msg.MSG_GAME_SCORE_ROW.format(x+1, games_results[x][0], games_results[x][1]))
        # Not guessed is false now
        print(msg.MSG_SEP_LINE)
        return False
    # Not guessed is still true
    return bool(True)

# Run the game
clear_screen()
print("Bulls & Cows \n")
# Multiple rounds with score allowed
while next_play:
    # Set basic control values for entire game
    start_time = time()
    not_done = bool(True)
    guess_counter = int(0)
    # Generate secret numbers
    secret_list = generate_secret_numbers([0, 0, 0, 0])
    # print(secret_list)
    print(msg.MSG_WELCOME)
    # Game loop
    while not_done:
        guess_counter += 1
        # Get new guess from user
        guess_list = get_new_guess_from_user()
        # Count bulls and cows
        bulls, cows = evaluate_new_guess(guess_list, secret_list)
        # Print result for this guess
        not_done = results_of_the_round(bulls, cows, guess_list, guess_counter)
    # Another game?
    next_play = input(msg.MSG_NEXT_GAME).lower() == 'y'
# All games are done
