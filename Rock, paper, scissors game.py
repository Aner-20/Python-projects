import random
#While loop is necessary to make sure that the player have to pick one of the three arguments

while True:
    choices = ["rock", "paper", "scissors"]

    computer = random.choice(choices)
    player = None

    while player not in choices:

       player = input("rock, paper, or scissors?: ").lower() #allows even upper characters

#Win conditions
    if player == computer:
       print("computer: ", computer)
       print("player: ", player)
       print("Tie!")

    elif player == "rock":
     if computer == "paper":
       print("computer: ", computer)
       print("player: ", player)
       print("You lose")
     if computer == "scissors":
       print("computer: ", computer)
       print("player: ", player)
       print("You win!")

    elif player == "scissors":
     if computer == "rock":
       print("computer: ", computer)
       print("player: ", player)
       print("You lose")
     if computer == "paper":
        print("computer: ", computer)
        print("player: ", player)
        print("You win!")

    elif player == "paper":
     if computer == "rock":
       print("computer: ", computer)
       print("player: ", player)
       print("You win!")
     if computer == "scissors":
       print("computer: ", computer)
       print("player: ", player)
       print("You lose")


#allows the user to play again
    play_again = input("Play again? (yes/no): ").lower()

    if play_again != "yes":
        break

print("Bye!")

