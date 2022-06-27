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
        self.word_to_diplay = ""
        for letter in self.secrete_word:
            if letter in already_guessed:
                self.word_to_diplay += " " + letter + " " 
            else:
                self.word_to_diplay += " _ "

        print(f" Word to complete :  {self.word_to_diplay} ")
        return self.word_to_diplay
class Hangman:
    HANGMAN_PICS = ["", "O", "O-", "O-|", "O-|-", "O-|-<"]
    def __init__(self):
        self.HANGMAN_PICS = Hangman.HANGMAN_PICS

    def draw(self, incorrect_guessed):
        print(f" Remaining lives: {self.HANGMAN_PICS[incorrect_guessed]}")

        if incorrect_guessed == 5:
            print(" GAME OVER !!!, You are hanged !!!")
            print()


        
class Game:

    WRONG_ANSWER_PUTDOWNS = ["NOPE!",
                            "You had one JOB to do!!",
                             "Wow, you suck at hangman.",
                             "Your guy doesn't stand a chance!",
                             "You're leaving him high and dry"]

    def __init__(self) -> None:
        self.words = Words("words.txt")
        self.secrete_word = self.words.secrete_word

        self.hangman = Hangman()
        self.incorrect_guesses = 0
        self.already_guessed = []


    def play(self):
        print()
        print(" ##########   WELCOME TO HANGMAN   ######### ")
        print()

        option = input("Do you need the rules explained to you? Y/n:")

        if option.lower() == "y":
            print(" \nInstructions:\n ")
            print("A word will be chosen at random from the dictionary. Each turn you guess a letter.\n")
            print("Every time you guess a letter that isn't in the word, your man gets closer to being hanged!\n")
            print("When your hangman looks like this: O-|-< ...you're dead!\n")

        print("Lets Play HANGMAN !!!!!!")

        print()

        while self.incorrect_guesses < 5:
            if len(self.already_guessed) == 0:
                self.words.display(self.already_guessed)

            entered_letter = input(" Please guess a letter: ").lower()

            while not entered_letter.isalpha():
                entered_letter = input("No special characters are allowed, Please guess letters again :").lower()

            if entered_letter not in self.already_guessed:
                self.already_guessed.append(entered_letter)

                if entered_letter not in self.secrete_word:
                    

                    print()
                    print(random.choice(Game.WRONG_ANSWER_PUTDOWNS))
                    print()
                    self.incorrect_guesses += 1
                    self.hangman.draw(self.incorrect_guesses)
                    print()
                else:
                    print("Word is present !!,  Nice JOB !!")
                    #self.words.display(self.already_guessed)
                    self.hangman.draw(self.incorrect_guesses)

            else:
                print(f" You already have guessed {entered_letter}, try to guess different letter ")

            current_word = self.words.display(self.already_guessed)

            if "_" not in current_word:
                print("CONGOOOO!!! , YOU WON !!")
                break

            
game = Game()
game.play()
print(f" Secrete Word - {game.secrete_word} ")


