import random
import wordslist

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
while True:
    def user_input():
        guess = input("pick a letter\n")
        if guess in string_to_list:
            index = word.index(guess)
            empty_word[index] = guess
            print(empty_word)
        else:
            print("wrong answer")
    user_input()

# 6 questions will complete hangman and game is over
