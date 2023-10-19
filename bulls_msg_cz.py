""" Czech messages for the Bulls and Cows game - bulls.py """
MSG_LANGUAGE = "Czech"
MSG_WELCOME = """Zdravím!
-----------------------------------------------
Vygeneroval jsem pro tebe čtyři náhodná čísla.
Zkus je uhodnout - zahraj si Bulls and Cows!
-----------------------------------------------
Zadej čtyři čísla:"""
MSG_INPUT = ">>> "
MSG_SEP_LINE = "-----------------------------------------------"
MSG_BAD_INPUT = "Je nutné zadat čtyři a to různá čísla"
MSG_FINAL_RESULT = """Správně, uhodl jsi správnou kombinaci všech čísel 
a potřeboval jsi {} pokusů!"""
MSG_BULLS = {True : "bull", False : "bulls"}
MSG_COWS = {True : "cow", False : "cows"}
MSG_EVALUTION_GRADES = {0 : "skvělé", 1 : "průměrné", 2: "horší", 3: "špatné"}
MSG_EVALUATION = "Což je {}"
MSG_TIME_ELAPSED = "Čas potřebný na hru byl {} vteřin"
MSG_NEXT_GAME = "Další hru (Y/N)? "
MSG_GAME_SCORE = "Skóre"
MSG_GAME_SCORE_ROW = "Hra {}: {} pokusů během {} vteřin"