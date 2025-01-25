import random

def generate_code():
    """Generates a 4-digit code with digits between 1 and 6."""
    return [random.randint(1, 6) for _ in range(4)]

def validate_guess(guess):
    """Validates the user's guess."""
    if len(guess) != 4 or not all(char.isdigit() for char in guess):
        return False
    guess_digits = [int(char) for char in guess]
    return all(1 <= digit <= 6 for digit in guess_digits)

def evaluate_guess(code, guess):
    """Evaluates the guess against the code and provides feedback."""
    black_pegs = 0  # Correct color and position
    white_pegs = 0  # Correct color but wrong position

    code_copy = code[:]
    guess_copy = guess[:]

    # Check for black pegs
    for i in range(4):
        if guess_copy[i] == code_copy[i]:
            black_pegs += 1
            code_copy[i] = guess_copy[i] = None

    # Check for white pegs
    for i in range(4):
        if guess_copy[i] is not None and guess_copy[i] in code_copy:
            white_pegs += 1
            code_copy[code_copy.index(guess_copy[i])] = None

    return black_pegs, white_pegs

def play_game():
    """Main game logic."""
    print("Welcome to GameInt!")
    print("Guess the 4-digit code. Each digit is between 1 and 6.")
    print("Enter '0000' to quit the game.")

    code = generate_code()
    attempts = 0
    max_attempts = 8

    while attempts < max_attempts:
        guess_input = input(f"Attempt {attempts + 1}: Enter your guess: ")
        if guess_input == "0000":
            print("You chose to quit the game. Thanks for playing!")
            break

        if not validate_guess(guess_input):
            print("Invalid input! Please enter a 4-digit number with digits between 1 and 6.")
            continue

        guess = [int(char) for char in guess_input]
        black_pegs, white_pegs = evaluate_guess(code, guess)
        attempts += 1

        print(f"Result: {'1 ' * black_pegs}{'0 ' * white_pegs}")

        if black_pegs == 4:
            print(f"Congratulations! You guessed the code {''.join(map(str, code))} in {attempts} attempts.")
            break
    else:
        print(f"You've used all {max_attempts} attempts. The code was {''.join(map(str, code))}. Better luck next time!")

def main():
    """Main menu for the game."""
    while True:
        print("\nMenu:")
        print("1. Start Game")
        print("2. Quit")
        choice = input("Enter your choice: ")

        if choice == "1":
            play_game()
        elif choice == "2":
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please select 1 or 2.")

if __name__ == "__main__":
    main()
