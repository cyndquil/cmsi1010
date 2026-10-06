import random

secret = random.randint(1, 1000)

attempts = 0
print(secret)

while True:
    guess = input("Guess a number between 1 and 1000 (or type 'bye' or 'exit' to quit): ")
    
    if guess.lower() in ['bye', 'exit']:
        print("Goodbye!")
        break
    
    if not guess.isdigit():
        print("Please enter a valid number.")
        continue
    
    guess = int(guess)

    attempts += 1
    
    if guess < secret:
        print("Too low!")
    elif guess > secret:
        print("Too high!")
    else:
        print(f"Congratulations! You guessed the number {secret}!" f" It took you {attempts} attempts.")
        secret = random.randint(1, 1000)
        attempts = 0
        print(secret)