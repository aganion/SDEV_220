"""
Alicia Ganion
2/4/2026
Loops and Conditionals
"""

#6.1

secret = 4
guess = int(input("Try and guess the secret number. Enter a number between 1 and 10: "))

while guess != secret:
    if guess < 1 or guess > 10:
        guess = int(input(f"{guess} is not a valid entry. Please enter a number between 1 and 10: "))
    elif guess > secret:
        guess = int(input(f"{guess} is greater than the secret number. Guess another number between 1 and 10: "))
    elif guess < secret:
        guess = int(input(f"{guess} is less than the secret number. Guess another number between 1 and 10: "))

while guess == secret:
    print(f"Congratulations! You have guess the secret number: {secret}")
    break

#6.2

user_small = input("Is your object small? Y or N: ").upper()
user_green = input("Is your object green? Y or N: ").upper()

while user_small == "Y" or "N" and user_green == "N" or "Y":
    if user_small == "Y" and user_green == "Y":
        print("Since your object is small and green, it must be a pea!")
        break
    elif user_small == "Y" and user_green == "N":
        print("Since your object is small, but not green, it must be a cherry!")
        break
    elif user_small == "N" and user_green == "Y":
        print("Since your object is not small, but green, it must be a watermelon!")
        break
    elif user_small == "N" and user_green == "N":
        print("Since your object is not small and not green, it must be a pumpkin!")
        break
    else:
        print("Sorry that is an invalid response.")
        user_small = input("Is your object small? Y or N: ").upper()
        user_green = input("Is your object green? Y or N: ").upper()

#7.1
user_list = [3, 2 , 1, 0]
for item in user_list:
    print(item)

#7.2
guess_me = 7
number = 1

while True:
    if number < guess_me:
        print("Guess is too low.")
    elif number > guess_me:
        print("Guess is too high.")
        break
    elif number == guess_me:
        print("You found it!")
        break
    else:
        print("Oops, guess is not valid.")
        break
    number += 1

#7.3
guess_me = 5

for number in range(10):
    if number < guess_me:
        print("Guess is too low.")
    elif number > guess_me:
        print("Guess is too high.")
    elif number == guess_me:
        print("You found it!")
        break
    else:
        print("Oops, guess is not valid.")
        break