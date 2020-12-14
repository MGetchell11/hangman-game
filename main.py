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
# Find indexes of correct letters and replace the blank spaces with correct letters
while True:
    def user_input():
        guess = input("pick a letter\n")
        if guess in string_to_list:
            all_indexes = []
            for i in range(0, len(string_to_list)):
                if string_to_list[i] == guess:
                    all_indexes.append(i)
                    empty_word[i] = guess
                    print(empty_word)
        else:
            attempt = 0
            while attempt > 6:
                attempt = attempt + 1
                print(attempt)


    user_input()

# 6 wrong guesses and the game is over
