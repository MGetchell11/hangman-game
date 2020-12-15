import random
import wordslist
import sys
import graphic

# Pick random word from wordslist.py
word = random.choice(wordslist.words_list)

# Split word from string into list
string_to_list = list(word)
print(string_to_list)

# Empty string for correct letters
num_asterisks = len(word) * "_"
empty_word = list(num_asterisks)
print(empty_word)

# User input loop
# Find indexes of correct letters and replace the blank spaces with correct letters

def game():
    wrong_answers = 0
    while True:
        guess = input("pick a letter\n")
        if guess in string_to_list:
            all_indexes = []
            for i in range(0, len(string_to_list)):
                if string_to_list[i] == guess:
                    all_indexes.append(i)
                    empty_word[i] = guess
                    print(empty_word)
                    if "_" not in empty_word:
                        print("You win!")
                        sys.exit()
                    else:
                        continue
                else:
                    continue
        else:
            wrong_answers += 1
            print(wrong_answers)
            if wrong_answers == 0:
                continue
            elif wrong_answers == 1:
                graphic.first_wrong()
                continue
            elif wrong_answers == 2:
                graphic.second_wrong()
                continue
            elif wrong_answers == 3:
                graphic.third_wrong()
                continue
            elif wrong_answers == 4:
                graphic.fourth_wrong()
                continue
            elif wrong_answers == 5:
                graphic.fifth_wrong()
                continue
            elif wrong_answers == 6:
                graphic.sixth_wrong()
                print("You Lost")
                sys.exit()
            continue
game()
