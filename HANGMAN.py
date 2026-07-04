# %%
import random
words = ["apple", "tiger", "chair", "robot", "pencil"]
secret_word = random.choice(words)
guessed_word = ["_"] * len(secret_word)
attempts = 6
guessed_letters = []

print("===================================")
print("      WELCOME TO HANGMAN GAME")
print("===================================")
print("Guess the word one letter at a time.")
print("You have 6 incorrect guesses.\n")
while attempts > 0 and "_" in guessed_word:
    print("\nCurrent Word:", " ".join(guessed_word))
    print("Guessed Letters:", " ".join(guessed_letters))
    print("Remaining Attempts:", attempts)
    guess = input("\nEnter a letter: ").lower()
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one alphabet letter.")
        continue
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)
    if guess in secret_word:
        print("Correct Guess!")
        for i in range(len(secret_word)):
            if secret_word[i] == guess:
                guessed_word[i] = guess

    else:
        print("Wrong Guess!")
        attempts -= 1
print("\n==============================")

if "_" not in guessed_word:
    print("🎉 Congratulations!")
    print("You guessed the word:", secret_word.upper())
else:
    print("💀 Game Over!")
    print("The correct word was:", secret_word.upper())

print("==============================")



# %%
