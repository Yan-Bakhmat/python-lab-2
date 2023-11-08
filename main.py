from plus import game_over
import random
import pickle

colors = ['red', 'blue', 'green']
new_list = colors
colors_copy = colors.copy()
random.shuffle(colors)
print(f"{colors}, id: {id(colors)}")
print(f"{new_list}, id: {id(new_list)}")
print(f"{colors_copy}, id: {id(colors_copy)}")

"""
Коли ми створили нову змінну "new_list" та присвоїли їй значення змінної "colors", насправді, ми не робимо її копію, а лише зберігаємо посилання на неї.
В цьому легко впевнитись за допомогою функції id(). Бачимо, що їхні id однакові, а отже при зміні однієї зі змінних змінюється й друга.
Щоб уникнути цього та створити повноцінну незалежну копію, варто скористатися методом .copy(), про що свідчить наведений приклад зі змінною "colors_copy".
"""

# HANGMAN game

load_file = open('words.dat', 'rb')
word_list = pickle.load(load_file)
load_file.close()

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
        guess = input("Guess a letter: ").lower()
        if guess in attempts:
            print("You already checked this letter, try another one.")
        else:
            attempts.append(guess)
            test = False
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
    game_over()
