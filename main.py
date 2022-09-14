import random
import art
import words


chosen_word = random.choice(words.word_list)  # Sets the word to guess randomly from the file "words"

print(art.logo)  # Prints the Game's logo

game_over = False
lives = 6
word_length = len(chosen_word)

display = ['_'] * word_length  # Creates a list of '_' characters matching the number of letters in the word

print(*display)  # Prints the "display" list items side by side E.g. word is "apple" -> _ _ _ _ _

while not game_over:  # Game Loop
    guess = input("Guess a letter: ").lower()  # Gets the user input and converts it to lowercase

    if guess in display:  # Checks if player already guessed this letter
        print(f"You've already guessed {guess}")
        print(art.stages[lives])  # Prints the hangman art according to "lives" variable
        continue  # Makes sure the player isn't punished for trying a letter they already went for

    for position in range(word_length):  # Checks if the letter exists and wherever it does, it replaces the '_'
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter  # Replaces the '_' at that index of "display" with the guessed letter

    if guess not in chosen_word:  # if the player chose a wrong letter, it punishes them
        print(f"you guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1  # Decreases the "lives" variable by 1
        if lives == 0:  # Game-ending condition 1/2
            game_over = True  # Redundant but makes the code easier to read
            print("you lose :(")
            print(f'The word was {chosen_word}')
            print(art.stages[lives])  # Prints the hangman art according to "lives" variable
            break  # break is inserted to prevent a useless print of "display"

    print(*display) # Prints the "display" list again incase any changes were made
    print(art.stages[lives])  # Prints the hangman art according to "lives" variable

    if '_' not in display:  # Game-ending condition 2/2
        game_over = True  # Redundant but makes the code easier to read
        print("you won!")
        break # break is inserted to prevent a useless print of "display"

