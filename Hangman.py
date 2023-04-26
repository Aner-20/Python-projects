import random
from Words import words
import string

def get_valid_word(words):
    word = random.choice(words)
    while "-" in word or " " in word:
        word = random.choice(words)

    return word.upper()


def hangman():
    word = get_valid_word(words)
    word_letters = set(word) #letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set() #what the user has guessed
    lives = 6

    # getting user input

    while len(word_letters) > 0 and lives > 0:  #^ iterate till the user guess the word
        # letters used

        print(" You have", lives, "lives left and you have used these letters: ", '' .join(used_letters))

        # what does .join?  ---> ' '.join([ 'a', 'b', 'cd')] ---> 'a b cd' Turn a list into a string
        # what current word is (ie W -R D) (tell this to the user, the word that he has to guess)

        word_list = [letter if letter in used_letters else '-' for letter in word]
        print("Current word: ", '  '.join(word_list))
        user_letter = input("Guess a letter: ").upper()


        if user_letter in alphabet - used_letters: # if this is a valid char in the alphabet i can add to the list
             used_letters.add(user_letter)

        # if the letter guessed by the user is in the words of list, it removes from word_letter

             if user_letter in word_letters:
                  word_letters.remove(user_letter)

             else:
                 lives = lives - 1  # takes away a life if wrong
                 print("Letter is not in word. ")


        # if the user has already used a letter

        elif user_letter in used_letters:
            print("You have already used that letter. Try again. ")

        # if the user type a wrong character

        else:
            print("invalid character. Try again. ")  #^

    # gets here when len(word_letters) == 0 or when lives == 0

    if lives == 0:
        print("You lost, sorry. The word was", word)

    else:
        print("You guessed the word", word, '!!')



hangman()


