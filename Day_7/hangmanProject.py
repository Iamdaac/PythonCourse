import random
from hangman_art import logo, stages
from hangman_words import word_list

print(logo)

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)

for position in range(word_length):
    placeholder += "_"
print(placeholder)

lives = 6
lives == stages
game_over = False
correct_letters = [] #If this list was in the while loop, it would be clear every time it loop
guessed_letters = []

while not game_over:
    display = ""

    guess = input("Guess a letter: ").lower()

    if guess in guessed_letters:
        print(f"You've already guessed '{guess}'. Try another letter.")
        continue
    else:
        guessed_letters.append(guess)

    for letter in chosen_word: 
        if letter == guess: 
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters: 
            display += letter
        else: 
            display += "_"


    print(display)

    if guess not in chosen_word: 
        lives -=1
        print(lives, "Lives left")
        print(stages[lives])
        print(f"The {guess} is not in the word.")

        if lives == 0:
            game_over = True
            print("You Lose!")
            print(f"You lose! The word was: {chosen_word}")

    if "_" not in display:
        game_over = True
        print("You win!")



