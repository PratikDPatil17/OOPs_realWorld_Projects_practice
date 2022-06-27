import random


class Words:
    def __init__(self, filename):
        self.filename = filename
        self.word_list = []
        

        with open(filename) as f:
            for line in f:
                self.word_list.append(line.rstrip())

        self.secrete_word = random.choice(self.word_list)

    def display(self, already_guessed):
        word_to_display = ""

        for letter in self.secrete_word:
            if letter in already_guessed:
                word_to_display += " "+letter+" "
            else:
                word_to_display += " _ "

        print(f" Secrete word : {word_to_display}")
        return word_to_display

# class Hangman:
#     def __init__(self) -> None:
#         pass
        
class Game:
    def __init__(self) -> None:
        self.words = Words("words.txt")
        self.secrete_word = self.words.secrete_word

        self.incorrect_guesses = 0
        self.already_guessed = []

    # def enter_letter(self):
    #     self.entered_letter = input("Guess the letter").lower()
        # if not self.entered_letter.isalpha():
        #     print("Only letters are allowed")
        #     self.enter_letter()
            
        #entered_letter = input("Guess the letter").lower()

    def play(self):
        print()
        print(" ########    WELCOME HANGMAN     ########")

        # do you want to display Rules or not
        option = input("Do you need the rules explained to you? Y/n:")

        if option.lower() == "y":
            print(" \nInstructions:\n ")
            print("A word will be chosen at random from the dictionary. Each turn you guess a letter.\n")
            print("Every time you guess a letter that isn't in the word, your man gets closer to being hanged!\n")
            print("When your hangman looks like this: O-|-< ...you're dead!\n")

        print("Lets Play HANGMAN !!!!!!")

        print()

        #guessed_word = self.words.display(self.already_guessed)
        
        while self.incorrect_guesses < 5:
            if len(self.already_guessed) == 0:
                self.words.display(self.already_guessed)
            print(f" Wrong guesses  : {self.incorrect_guesses} ")
            entered_letter = input(" Please guess a letter: ").lower()

            while not entered_letter.isalpha():
                entered_letter = input("No special characters are allowed, Please guess letters again :").lower()


            # new letter 
            if entered_letter not in self.already_guessed:
                self.already_guessed.append(entered_letter)

                # if that letter not present in secrete word
                if entered_letter not in self.secrete_word:
                    self.incorrect_guesses += 1
                    print("Guess the right letter this time")
                
                # if entered letter present in secrete word
                else:
                    #guessed_word = self.words.display(self.already_guessed)
                    print("Word is present !!,  Nice JOB !!")

                    #entered_letter = self.enter_letter()

            # if already guessed
            else:
                print(f" You already have guessed {entered_letter}, try to guess different letter ")


            guessed_word = self.words.display(self.already_guessed)
            if "_" not in guessed_word:
                print(" Congo!!!! You saved yourself ")
                break
            

game = Game()
game.play()


