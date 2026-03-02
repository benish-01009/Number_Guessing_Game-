import random

def play_game():
    secret_number = random.randint(1, 100)
    attempts = 0

    print("\nWelcome to the Number Guessing Game!")
    print("I have selected a number between 1 and 100.")

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < secret_number:
                print("Too low! Try again.")

            elif guess > secret_number:
                print("Too high! Try again.")

            else:
                print("Congratulations! You guessed correctly.")
                print("Total attempts:", attempts)
                break

        except ValueError:
            print("Please enter a valid number!")

def main():
    while True:
        play_game()
        again = input("\nDo you want to play again? (yes/no): ").lower()

        if again != "yes":
            print("Thank you for playing!")
            break

main()



