import random
import re


def number_guessing_game():
    print("\n==============================")
    print("     NUMBER GUESSING GAME")
    print("==============================")

    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 10
    score = 100

    print("I have selected a number between 1 and 100.")
    print(f"You have {max_attempts} attempts to guess it.")

    while attempts < max_attempts:
        try:
            guess = int(input("\nEnter your guess: "))
        except ValueError:
            print("Invalid input! Please enter a whole number.")
            continue

        if guess < 1 or guess > 100:
            print("Please enter a number between 1 and 100.")
            continue

        attempts += 1

        if guess == secret_number:
            print("\nCongratulations! You guessed the number!")
            print("Number of attempts:", attempts)
            print("Your score:", score)
            return

        elif guess < secret_number:
            print("Too low! Try a higher number.")
        else:
            print("Too high! Try a lower number.")

        score -= 10
        print("Attempts remaining:", max_attempts - attempts)

    print("\nGame Over!")
    print("The correct number was:", secret_number)
    print("Your final score:", max(score, 0))


def word_frequency_counter():
    print("\n==============================")
    print("       WORD COUNTER")
    print("==============================")

    filename = input(
        "Enter text file name (default: sample_text.txt): "
    )

    if filename.strip() == "":
        filename = "sample_text.txt"

    try:
        with open(filename, "r", encoding="utf-8") as file:
            text = file.read()

    except FileNotFoundError:
        print("Error: File not found.")
        print("Make sure the text file is in the same folder.")
        return

    words = re.findall(r"\b[a-zA-Z0-9]+\b", text.lower())

    total_words = len(words)
    unique_words = len(set(words))

    frequency = {}

    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1

    print("\n----- Word Analysis -----")
    print("Total words:", total_words)
    print("Unique words:", unique_words)

    print("\nWord Frequency:")

    sorted_frequency = sorted(
        frequency.items(),
        key=lambda item: item[1],
        reverse=True
    )

    for word, count in sorted_frequency:
        print(f"{word}: {count}")


def main():
    while True:
        print("\n==============================")
        print(" NUMBER GUESSING & WORD COUNTER")
        print("==============================")
        print("1. Number Guessing Game")
        print("2. Word Frequency Counter")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            number_guessing_game()

        elif choice == "2":
            word_frequency_counter()

        elif choice == "3":
            print("Thank you for using the program!")
            break

        else:
            print("Invalid choice! Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()
