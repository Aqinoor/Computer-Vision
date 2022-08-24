from importlib.machinery import WindowsRegistryFinder
import random


class RPS:
    def __init__(self):
        self.user_wins = 0
        self.computer_wins = 0
        self.choices = ['Rock', 'Paper', 'Scissors']

    def get_computer_choice(self):
        return random.choice(self.choices)

    # randomly take an option from choices and assigned it to computer_choice
    # Return computer_choice

    def get_user_choice(self):
        user_choice = input("Enter Rock, Paper or Scissors")
        return user_choice

    def get_winner(self, user_choice, computer_choice): # 0 = Draw, 1 = User winner, 2 Computer winner
        if user_choice == computer_choice:
            return 0
        elif user_choice == 'Rock':
            if computer_choice == 'Scissors':
                return 1
            else:
                return 2
        elif user_choice == 'Paper':
            if computer_choice == 'Rock':
                return 1
            else:
                return 2
        elif user_choice == 'Scissors':
            if computer_choice == 'Paper':
                return 1
            else:
                return 2
        