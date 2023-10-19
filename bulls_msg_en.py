""" English messages for the Bulls and Cows game - bulls.py """
MSG_LANGUAGE = "English"
MSG_WELCOME = """Hi there!
-----------------------------------------------
I've generated a random 4 digit number for you.
Let's play a Bulls and Cows game.
-----------------------------------------------
Enter a number:"""
MSG_INPUT = ">>> "
MSG_SEP_LINE = "-----------------------------------------------"
MSG_BAD_INPUT = "Enter 4 unique digits please"
MSG_FINAL_RESULT = """Correct, you've guessed the right number 
in {} guesses!"""
MSG_BULLS = {True : "bull", False : "bulls"}
MSG_COWS = {True : "cow", False : "cows"}
MSG_EVALUTION_GRADES = {0 : "amazing", 1 : "average", 2: "not so good", 3: "bad"}
MSG_EVALUATION = "That's {}"
MSG_TIME_ELAPSED = "Elapsed time {} seconds"
MSG_NEXT_GAME = "Another game Y/N)? "
MSG_GAME_SCORE = "Score"
MSG_GAME_SCORE_ROW = "Game {}: {} guesses in {} seconds"