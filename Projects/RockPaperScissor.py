import random

def get_choices():
    player_choice = input("Enter a choice (rock, paper, scissor): ")

    options = ["rock", "paper", "scissor"]
    computer_choice = random.choice(options)
    choices = {"player": player_choice, "computer": computer_choice}

    return choices



def check_win(player, computer):
    print(f"You chose: {player}, Computer chose: {computer}")
    
    if player == computer :
        return ("It's a tie!")
    elif player == "rock":
        if computer == "scissor":
            return "Rock samshes Scissors ! You WIN"
        else:
            return "Paper covers Rock ! You LOSE"
    elif player == "paper":
        if computer == "scissor":
            return "Scissors cuts Paper ! You LOSE"
        else:
            return "Paper covers Rock ! You WIN"
    elif player == "scissor":
        if computer == "rock":
            return "Rock samshes Scissors ! You LOSE"
        else:
            return "Scissor cuts Paper ! You WIN"




choices = get_choices()
result = check_win(choices["player"], choices["computer"])


print(result)