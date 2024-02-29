"""importamos textblob"""

from textblob import TextBlob
from colorama import Fore


RED = Fore.RED
GREEN = Fore.GREEN


# Enunciado
print(RED + "you can check words from here...")
print(RED + "to exit the program type 0")

# key gives out
EXIT = 0

# We declare an empty list where each word that the user writes will go.
list_of_corrected_words = []
while True:

    # we declare variables to use
    words = input("Enter the words you want to correct or know how to spell: ")
    if words == "0":
        print(RED + "see you...")
        break

    list_of_corrected_words.append(TextBlob(words))
    for i in list_of_corrected_words:
        print(i.correct())
