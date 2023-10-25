import random

computer_score = 0
user_score = 0
x = ("rock", "paper", "scissor")


def score():
    print("User's choice :", user_input)
    print("Computer's Choice :", computer_choice)


while True:
    user_input = input("Select Rock/Paper/Scissors or 'q' to Quit:").lower()
    computer_choice = random.choice(x)
    if user_input == 'q':
        break
    elif user_input not in x and user_input != "q":
        print("Wrong input,Please Enter again")
    elif (user_input == 'rock') and (computer_choice == 'scissor'):
        user_score += 1
        score()
        print("User Wins")
    elif (user_input == 'paper') and (computer_choice == "rock"):
        user_score += 1
        score()
        print('User Wins')
    elif (user_input == 'scissor') and (computer_choice == 'paper'):
        user_score += 1
        score()
        print('User Wins')
    elif user_input == computer_choice:
        score()
        print('Draw')
    else:
        computer_score += 1
        score()
        print("Computer Wins")

if computer_score > user_score:
    print("USER LOST")
elif computer_score == user_score:
    print("THE MATCH IS DRAW")
else:
    print("USER WINS")

print("Computer Score ", computer_score)
print("User Score", user_score)
