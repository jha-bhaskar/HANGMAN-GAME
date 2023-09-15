import random
import word_file
import hanging_man
health=6
chosen_word=random.choice(word_file.words)
display=[]
for i in range(len(chosen_word)):
    display += '_'
print(display)
game_over=False
while not game_over:
    gussed_letter=input("Guess a letter \n").lower()
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == gussed_letter:
            display[position]=gussed_letter
    print(display)        

    if gussed_letter not in chosen_word:
        health -= 1
        if health == 0:
            game_over=True
            print("You Lose !!")
    if '_' not in display:
        game_over = True
        print("You Win !!")
    print(hanging_man.hangman_stages[health])





