import random

class RPS:
    def __init__(self):
        self.user_wins = 0
        self.computer_wins = 0
        self.choices = ['Rock', 'Paper', 'Scissors']

    def get_computer_choice(self):
        computer_choice = random.choice(self.choices)
        return computer_choice

    def get_user_choice(self):
    
        user_choice = input("Choose Rock, Paper or Scissors: ")
        return user_choice
        

    def get_winner(self, user_choice, computer_choice): # 0 = Draw, 1 = User winner, -1 Computer winner
        if user_choice == computer_choice:
            print(f"'computer_choice': {computer_choice}, 'user_choice': {user_choice}") 
            print("Draw!") 
        elif (user_choice == 'Rock' and computer_choice == 'Scissors') or \
             (user_choice == 'Paper' and computer_choice == 'Rock') or \
             (user_choice == 'Scissors' and computer_choice == 'Paper'):
            print(f"'computer_choice': {computer_choice}, 'user_choice': {user_choice}")
            self.user_wins += 1
            print("User Wins") 
        else:
            print(f"'computer_choice': {computer_choice}, 'user_choice': {user_choice}")
            self.computer_wins += 1
            print("Computer Wins")
            
def play(choice):
    rounds = 0
    game = RPS()
    while game.user_wins < 3 or game.computer_wins < 3:      
        computer_choice = game.get_computer_choice() 
        user_choice = game.get_user_choice()
        game.get_winner(user_choice, computer_choice)
        if game.user_wins == 3:
            print("You won!")
            exit()
        elif game.computer_wins == 3:
            print("You lose!")
            exit()
    
    
if __name__ == '__main__':
    choice = ["Rock", "Paper", "Scissors"]
    play(choice)
        







