import random  # import random module

colors = ['red', 'blue', 'green']  # create list
new_list = colors  # duplicate list to new variable
random.shuffle(colors)
print(new_list)  # what is the expected outcome of this output? Why?

# Create list
word_list = ["aardvark", "baboon", "camel"]

# Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = random.choice(word_list)
print(chosen_word)

display = []
for _ in chosen_word:
    display.append('_')

end_of_game = False
lives = 6
attempts = []
while lives != 0 and display != list(chosen_word):
    test = True
    while test:
        # Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
        guess = input("Guess a letter: ").lower()
        if guess in attempts:
            print("You already checked this letter, try another one.")
        else:
            attempts.append(guess)
            test = False
    # Check if the letter the user guessed (guess) is one of the leters in the chosen_word.
    if guess in chosen_word:
        for i in range(len(chosen_word)):
            if chosen_word[i] == guess:
                display[i] = guess
        print("Right", display)
    else:
        print("Wrong", display)
    lives -= 1
if display == list(chosen_word):
    print("YOU WIN!")
else:
    print("GAME OVER!")
