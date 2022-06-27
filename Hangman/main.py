import random
import sys
from traceback import print_last


class Words:
    def __init__(self, filename) -> None:
        self.filename = filename
        self.word_list = []

        with open (self.filename) as f:
            
            for line in f:
                self.word_list.append(line.rstrip())

        self.word = random.choice(self.word_list)
        
    def choose_random_word(self):
        return self.word

    def display(self, guessed_letter_list):
        word_to_display = ""
        for letter in self.word:
            if letter in guessed_letter_list:
                word_to_display += " " + letter + " "
            else:
                word_to_display += " _ "

        print(f"This is your word so far {word_to_display}")
        return word_to_display

class Hangman:

    HANGMAN_PICS = ["", "O", "O-", "O-|", "O-|-", "O-|-<"]

    def __init__(self) -> None:
        self.hangman = Hangman.HANGMAN_PICS[0]

        
    def draw(self, num_incorrect_guesses):
        self.hangman = self.HANGMAN_PICS[num_incorrect_guesses]

        print(self.hangman)

        if num_incorrect_guesses == 5:
            print("You Died!!")
            print()


class Game:

    WRONG_ANSWER_PUTDOWNS = ["NOPE!",
                             "Wow, you suck at hangman.",
                             "Your guy doesn't stand a chance!",
                             "You're leaving him high and dry"]   

    
    def __init__(self, filename) -> None:
        self.secrete_word = Words(filename)
        self.random_word = self.secrete_word.choose_random_word()
        
        self.hangman = Hangman()
        self.incorrect_num_guess = 0
        self.guessed_letters = []


    def play(self):

        """ New game Hungman game begins """

        print()
        print("################## Welcome to Hangman ##################")

        option = input("Do you need the rules explained to you? Y/n:")

        if option.lower() == "y":
            print(" \nInstructions:\n ")
            print("A word will be chosen at random from the dictionary. Each turn you guess a letter.\n")
            print("Every time you guess a letter that isn't in the word, your man gets closer to being hanged!\n")
            print("When your hangman looks like this: O-|-< ...you're dead!\n")

        print("Lets Play HANGMAN !!!!!!")


        while self.incorrect_num_guess < 5:
            if len(self.guessed_letters) == 0:
                self.secrete_word.display(self.guessed_letters)

            letter_guess = input("Please guess a letter: ").lower()

            while not letter_guess.isalpha():
                letter_guess = input("No special Characters allowed! Only enter a letter, Please!! = ").lower()

            if letter_guess not in self.guessed_letters:
                self.guessed_letters.append(letter_guess)

                if letter_guess not in self.secrete_word.word:
                    print(random.choice(self.WRONG_ANSWER_PUTDOWNS))
                    self.incorrect_num_guess += 1

                    self.hangman.draw(self.incorrect_num_guess)


                else:
                    print("Relieved !! word present ")
                    self.hangman.draw(self.incorrect_num_guess)

            else:
                print(f"You already have guessed this letter {letter_guess}, Please choose new letter !!! ")

            current_word = self.secrete_word.display(self.guessed_letters)

            #print(f"Current guessed letters in word {current_word}")

            if "_" not in current_word:
                print("You have WON !!!!  Congratulations!!! ")
                break



game = Game("words.txt")
game.play()
print()
print(f"Secrete word - {game.random_word}")
