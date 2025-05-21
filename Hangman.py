import random

# List of words for the game
words = ["python", "hangman", "coding", "superstar", "project"]

# Choose a random word
word = random.choice(words)
guesses = ''
turns = 6

print("Welcome to Hangman Game!")

# Game loop
while turns > 0:
    failed = 0
    print("\nWord: ", end='')

    for char in word:
        if char in guesses:
            print(char, end=' ')
        else:
            print("_", end=' ')
            failed += 1

    if failed == 0:
        print("\nCongratulations! You guessed the word:", word)
        break

    guess = input("\nGuess a letter: ").lower()

    if guess in guesses:
        print("You already guessed that letter.")
        continue

    guesses += guess

    if guess not in word:
        turns -= 1
        print("Wrong guess!")
        print("Turns left:", turns)

        if turns == 0:
            print("Game over! The word was:", word)
