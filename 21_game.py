import random
import csv
from colored import fg, bg, attr

import random
import csv
from colored import fg, bg, attr


print(f"{bg('green')}{fg('red')}Welcome to Counting to 21 Game{attr('reset')}")

import random
import csv
from colored import fg, bg, attr


print(f"{bg('green')}{fg('red')}Welcome to Counting to 21 Game{attr('reset')}")

def user_turn(current_total):
    valid_choices = [1, 2]
    max_choice = 2 if current_total < 20 else 1
    while True:
        try:
            choice = int(input(f"Current total: {current_total}\nYour turn, please enter 1 or 2: "))
            if choice in valid_choices and choice <= max_choice:
                return choice
            else:
                raise ValueError("Please enter 1 or 2 only: ")
        except ValueError as e:
            print(e)

