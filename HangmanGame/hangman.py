import random
from colorama import Fore, init
init(autoreset=True)
words = [
    "python",
    "computer",
    "developer",
    "programming",
    "keyboard",
    "software",
    "internet",
    "github",
    "algorithm",
    "codealpha"
]
word = random.choice(words)
guessed_letters = []
wrong_guesses = 0
max_wrong = 6
print(Fore.MAGENTA + "=" * 50)
print(Fore.YELLOW + "          🎮 HANGMAN GAME 🎮")
print(Fore.MAGENTA + "=" * 50)
print(Fore.CYAN + "\nGuess the hidden word!")
while wrong_guesses < max_wrong:
    display_word = ""
    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print(Fore.GREEN + "\nWord:", display_word)
    print(Fore.BLUE + f"Wrong Attempts Left: {max_wrong - wrong_guesses}")
    if "_" not in display_word:
        print(Fore.YELLOW + "\n🎉 Congratulations! You guessed the word:", word)
        break
    guess = input(Fore.CYAN + "\nEnter a letter: ").lower()
    if len(guess) != 1 or not guess.isalpha():
        print(Fore.RED + "Please enter only one alphabet.")
        continue
    if guess in guessed_letters:
        print(Fore.YELLOW + "You already guessed that letter.")
        continue
    guessed_letters.append(guess)
    if guess in word:
        print(Fore.GREEN + "✔ Correct Guess!")
    else:
        wrong_guesses += 1
        print(Fore.RED + "✘ Wrong Guess!")
if wrong_guesses == max_wrong:
    print(Fore.RED + "\n💀 Game Over!")
    print(Fore.YELLOW + "The correct word was:", word)
print(Fore.MAGENTA + "\nThank you for playing Hangman! 😊")