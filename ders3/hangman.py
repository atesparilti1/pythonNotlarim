from random import randint

name = input("Your name: ")
print("Welcome " + name + " Lets play hangman")

secret_words_list = ["script", "nominate", "responsible", "consultation", "systematic", "colleague", "reverse", "point",
                     "tissue", "error", "heaven", "reach", "password", "outline", "weapon"]
secret_word = secret_words_list[randint(0, len(secret_words_list) - 1)].lower()

lives = len(secret_word) + 3

guess_string = ""

while lives > 0:
    character_left = 0

    for character in secret_word:
        if character in guess_string:
            print(character)
        else:
            print("-")
            character_left += 1

    if character_left == 0:
        print("You have won")
        break

    guess = input("Guess a word: ")
    guess_string += guess.lower()

    if guess not in secret_word:
        lives -= 1
        print("Wrong")
        print(f"You have {lives} left")

        if lives == 0:
            print(f"The word was {secret_word} ")
            print("You have lost, good luck next time")
