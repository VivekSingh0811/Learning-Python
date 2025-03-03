import random

def get_choices():
    player_choice = input("Enter a choice (rock, paperr, scissor): ")
    # computer_choice = "paper"
    options = ["rock", "paper", "scissor"]
    computer_choice = random.choice(options)
    choices = {"player": player_choice, "computer": computer_choice}
    
    # return player_choice
    return choices

# choices = get_choices()
# print(choices)


# choices1 = get_choices
# print(choices1)
# This prints the location of function get_choices...


# def greeting():
#     return "Hi!!!"

# response = greeting()
# print(response)



# Dictionary :---
# dict = {"name": "Beau", "color": "Blue"}
# dict = {"name": "Beau", "color": choices}



# list :---
# food = ["pizza", "carrots", "eggs"]
# dinner = random.choice(food)
# print(dinner)


# f-string :---
# age = 25
# print(f"Jim is {age} years old.")


# if & elif statements :---
# age = 18
# if age>=18:
#     print("Youm are an Adult")
# elif age>=12:
#     print("You are a teenager")
# elif age>1:
#     print("You are a child")
# else:
#     print("You are a Baby")



# def check_win(player, computer):
#     # print("You Chose: " + player, "Computer Chose: " + computer)
#     print(f"You chose: {player}, Computer chose: {computer}")
#     if player == computer :
#         # return "It's a tie"
#         return ("It's a tie!")
#     elif player == "rock" and computer == "scissor":
#         return "Rock samshes Scissors ! You WIN"
#     elif player == "rock" and computer == "paper":
#         return "Paper covers Rock ! You LOSE"



def check_win(player, computer):
    # print("You Chose: " + player, "Computer Chose: " + computer)
    print(f"You chose: {player}, Computer chose: {computer}")
    
    if player == computer :
        # return "It's a tie"
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


# check_win("rock", "paper")

choices = get_choices()
result = check_win(choices["player"], choices["computer"])
print(result)

