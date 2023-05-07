import random
from colored import fg, bg, attr
import csv


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


def computer_turn(current_total):
    valid_choices = [1, 2]
    max_choice = 2 if current_total < 20 else 1
    choice = random.choice(valid_choices[:max_choice])
    print(f"Computer chose {choice}.")
    return choice


def play_game():
    current_total = 0
    user_choice = None
    while current_total < 21:
        user_choice = user_turn(current_total)
        current_total += user_choice
        if current_total >= 21:
            print(f"{bg('red')}You are the winner!{attr('reset')}")
            with open("results.csv", "a")as results_file:
                writer = csv.writer(results_file)
                writer.writerow(["win"])
            break
        
        computer_choice = computer_turn(current_total)
        current_total += computer_choice
        if current_total >= 21:
            print(f"{bg('blue')}You are the loser!{attr('reset')}")
            with open("results.csv", "a")as results_file:
                writer = csv.writer(results_file)
                writer.writerow(["lose"])
            break

if __name__ == "__main__":
    play_game()


