import random

def game():
    # Generate a random number between 1 and 60
    num = random.randint(1, 60)
    
    if num == 42:
        print("You win!")
    else:
        print("Better luck next time.")

game()
