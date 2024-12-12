class LetterGuessingException(Exception):
    pass

class LetterComesBefore(LetterGuessingException):
    pass

class LetterComesAfter(LetterGuessingException):
    pass

class NotALetter(LetterGuessingException):
    pass

import time
from collections import defaultdict
from string import ascii_lowercase
from random import choice

class LetterGuessingGame:
    def __init__(self):
        self.start_time = time.time()
        self.performce = defaultdict(list)

    def _display_performance(self):
        time_taken = time.time() - self.start_time 
        print(f"You played this game for {time_taken} long.\n"
              f"You made {len(self.performce['before'])} guesses before the word\n"
              f"You made {len(self.performce['after'])} guesses after the word")

    def play(self):
        computer_choice = choice(list(ascii_lowercase))
        user_guess = None
        print(f"Computer has chosen a letter. Make your guess")

        while True:
            try:
                user_guess = input().strip().lower()
                
                if user_guess not in ascii_lowercase:
                    raise NotALetter
                elif user_guess > computer_choice:
                    raise LetterComesBefore
                elif user_guess < computer_choice:
                    raise LetterComesAfter
                
                print("Correct!")
                self._display_performance()

                break
            
            except LetterComesAfter:
                print("Nope, it was something after, guess again\n")
                self.performce["before"].append(user_guess)
            except LetterComesBefore:
                print("Nope, it was something before, guess again\n")
                self.performce["after"].append(user_guess)
            except NotALetter:
                print("Invalid Input\n")
            except KeyboardInterrupt:
                print("Game Interrupted!")
                self._display_performance()
                break
