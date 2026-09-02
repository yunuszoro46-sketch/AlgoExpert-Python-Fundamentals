import random

def get_int(prompt):
    while True:
        value = input(prompt)
        if value.isdigit():
            return int(value)
        print("Please enter a valid number.")

start = get_int("Enter the start of the range: ")

while True:
    end = get_int("Enter the end of the range: ")
    if end >= start:
        break
    print("Please enter a valid number.")

target = random.randint(start, end)
attempts = 0

while True:
    guess = get_int("Guess a number: ")
    attempts += 1
    if guess == target:
        break

if attempts == 1:
    print("You guessed the number in 1 attempt")
else:
    print(f"You guessed the number in {attempts} attempts")
