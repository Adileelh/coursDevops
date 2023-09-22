import random


def main():
    print("Welcome to the number guessing game!")
    print("I'm thinking of a number between 1 and 100.")
    print("Try to guess the number in as few attempts as possible.")
    print("")

    # Generate a random number between 1 and 100
    number = random.randint(1, 100)

    # Initialize the number of guesses the user has made
    num_guesses = 0

    # Obtain the user's first guess
    guess = int(input("Enter guess: "))
    num_guesses += 1

    # Loop until the user guesses correctly
    while guess != number:
        if guess > number:
            print("Lower...")
        else:
            print("Higher...")

        # Obtain the user's next guess
        guess = int(input("Enter guess: "))
        num_guesses += 1

    input()
