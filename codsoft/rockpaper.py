import random
def get_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (user == "rock" and computer == "scissors") or \
         (user == "scissors" and computer == "paper") or \
         (user == "paper" and computer == "rock"):
        return "You win!"
    else:
        return "You lose!"

while True:
    user_choice = input("Enter rock, paper, or scissors: ").lower()
    if user_choice not in ["rock", "paper", "scissors"]:
        print("Invalid input, try again.")
        continue

    
    computer_choice = random.choice(["rock", "paper", "scissors"])
    print("Computer chose:", computer_choice)

    
    result = get_winner(user_choice, computer_choice)
    print(result)

    
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("Thanks for playing!")
        break
