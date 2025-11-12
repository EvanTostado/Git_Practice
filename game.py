import random
print("Welcome to Rock-Paper-Scissors!")
choice = input("Choose rock, paper, or scissors: ")
print("You chose: " + choice)

RPS = ["Rock", "Paper", "Scissors"]
ComChoice = random.choice(RPS)
print(f"Computer chose: {ComChoice}")