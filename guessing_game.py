import random
import time

while True:
    number = random.randint(1, 100)
    print("Welcome to the Guessing Game!")

    print("Guess a number between 1 and 100")

    start_time = time.time()
    guess = int(input())

    if guess < number:
        print("Too low!")
    elif guess > number:
        print("Too high!")
    else:
        print("You win!")

    print(f"The number was {number}")
    print(f"Time taken: {time.time() - start_time:.2f} seconds")

    print("Play again? (y/n)")
    if input().lower() != 'y':
        break
