import random

num = random.randint(1, 500)

print("System selected a number from 1 to 500.")
print("Now it's your turn to guess!")

turns = 0

while True:

    guess = int(input("Enter the guessed number = "))
    turns += 1

    if guess == num:
        print("You got it right!")
        break

    elif guess < num:
        print("Bigger number please!")

    else:
        print("Lesser number please!")

print("Number of turns =", turns)