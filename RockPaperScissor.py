import random
import random

# Available choices
choices = ["rock", "paper", "scissors"]

print("🎮 Rock Paper Scissors Game")
print("Type rock, paper, or scissors")

user_choice = input("Your choice: ").lower()

# Validate input
if user_choice not in choices:
    print("❌ Invalid choice. Please choose rock, paper, or scissors.")
else:
    computer_choice = random.choice(choices)

    print(f"Computer chose: {computer_choice}")

    if user_choice == computer_choice:
        print("🤝 It's a tie!")
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "paper" and computer_choice == "rock") or
        (user_choice == "scissors" and computer_choice == "paper")
    ):
        print("🎉 You win!")
    else:
        print("💻 Computer wins!")
