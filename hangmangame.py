# Step 5

import random
from hangman_words import word_list
import hangman_art

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

# Create blanks
display = []
for _ in range(word_length):
    display += "_"

print(hangman_art.logo)
while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f'You have already guessed {guess}')

    # Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    # Check if user is wrong.
    if guess not in chosen_word:
        print(f'You chose {guess} and it is not in the word. You lose a life')
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")
            print(f'The word is actually {chosen_word}')

    # Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    # Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(hangman_art.stages[lives])
