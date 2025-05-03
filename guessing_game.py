import random

while True:
    number = random.randint(1, 50)
    print("Guess a number between 1 and 50")
    guess = int(input())

    if guess < number:
        print("Too low!")
    elif guess > number:
        print("Too high!")
    else:
        print("You win!")

    print(f"The number was {number}")
    
    print("Play again? (y/n)")
    if input().lower() != 'y':
        break
