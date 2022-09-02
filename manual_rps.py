import random

class RPS:
    def __init__(self):
        self.user_wins = 0
        self.computer_wins = 0
        self.choices = ['Rock', 'Paper', 'Scissors']

    def get_computer_choice(self):
        return random.choice(self.choices)

    def get_user_choice(self):
    
        user_choice = input("Choose Rock, Paper or Scissors: ")

        while True:
            if user_choice in choice:
                RPS.get_winner(self, user_choice)
                break
            else:
                print("Please enter either Rock, Paper or Scissors")
            break  
        pass
        

    def get_winner(self, user_choice, computer_choice): # 0 = Draw, 1 = User winner, -1 Computer winner
        if user_choice == computer_choice:
            return 0
        elif user_choice == 'Rock':
            if computer_choice == 'Scissors':
                return 1
            else:
                return -1
        elif user_choice == 'Paper':
            if computer_choice == 'Rock':
                return 1
            else:
                return -1
        elif user_choice == 'Scissors':
            if computer_choice == 'Paper':
                return 1
            else:
                return -1
        pass
            
def play(choice):
    game = RPS(choice)

    game.get_computer_choice()
    game.get_user_choice()
    pass

if __name__ == '__main__':
    choice = ["Rock", "Paper", "Scissors"]
    play(choice)
        







