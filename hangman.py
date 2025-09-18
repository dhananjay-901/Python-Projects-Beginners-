import time 
import random 
def choose_word():
    words = ['hangman','mother','father','brother','family','daughter','riverbed','refrigator','gallery','generator','country','government','bridge','flowerbed','canon','window']
    return random.choice(words)
def word_display(word):
    display_word = ''
    for i in word:
        if char in  guesses:
            display_word+=char+''
        else:             
            display_word += '_'
    return display_word

if __name__ == '__main__':
    word = choose_word()
    #print("word selected for this round is'" + word +"'")
    #print("string displayed during the game is", word_display(word))
    guesses = ''
    while True:
        print(word_display(word, guesses))
        guess = input("\nguess a character: ").lower()
        guesses+=guess