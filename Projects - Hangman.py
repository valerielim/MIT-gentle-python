# Name: Valerie Lim
# Date started; 9/2/2017
# Date completed:
# Title: Play Hangman game.py


def make_simple(listname):
     # listname is list of alphabets to be made
     # alphabets will be returned as lowercase word
     # E.g.: ['H', 'e', 'a', 'r'] = 'hear'
     # Note: will NOT work if numbers are present in list! 
     s = ""
     word = s.join(listname)
     str(word)
     word = str.lower(word)
     return word

# Test items for make_simple()
List1 = ['H', 'e', 'a', 'r']
List2 = ['a', 'p', 'p', 'l', 'e']
List3 = [0,1,2,3]

def maxval1(item):
     # item is a lit of integers
     # Uses a while loop
     index = 0
     while index < len(item):
          if item[index] < 6:
               print "yup"
               index = index + 1
          else:
               print "Eh bro. There is an element in this list greater than 6."
               break
     print "All items are less than 6."

# test objects
# positive= [1,5,3,4]
# negative = [5,3,7,5]

def maxval2(item, maxval):
     # item is a lit of integers
     # uses a for loop.
     # Will return if at least one item is greater than the max value stated
     # Will print if NOTHING is greater than value stated. 
     int(maxval)
     index = 0
     for i in item:
          if i > maxval:
               print "At least one item here is greater than max value defined."
               print "It is", str(i)+"."
               break
          else:
               index = index + 1
     if index == len(item):
          print "Nothing here is greater than the max value."

def maxval3(item, maxval):
     # item is a lit of integers
     # Will return if at least one item is LESS than the max value stated
     # Or, will return if ALL items are MORE than the max value. 
     int(maxval)
     index = 0
     for i in item:
          if i < maxval:
               print "At least one item here is lesser than max value defined."
               print "It is", str(i)+"."
               break
          else:
               index = index + 1
     if index == len(item):
          print "Nothing here is less than the max value."



# ---------------------Load Hangman Words---------------------

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split(" ")
    print "  ", len(wordlist), "words loaded."
    print 'Enter play_hangman() to play a game of hangman!'
    return wordlist

# actually load the dictionary of words and point to it with 
# the words_dict variable so that it can be accessed from anywhere
# in the program
words_dict = load_words()

def get_word():
    """
    Returns a random word from the word list
    """
    import random
    word=words_dict[random.randrange(0,len(words_dict))]
    return word

# ---------------------End of load words---------------------

def print_guessed(secret_word, letters_guessed):
          # Function returns letter(s) position in hangman word
          # if guessed correctly. 
          # Eg. Word = "claptrap", guesses = "ca"
          # Will return: "c-a--a-"          
     secret = list(secret_word)
     guesses = list(letters_guessed)
     tally = ""          # string
     for i in secret:
          if i not in guesses:
               tally = tally+"-"
               status = "incorrect"
          else:
               tally = tally+i
               status = "correct"
     return tally


def play_hangman():
     # Default = 6 chances for mistakes
     print "Let's play a game of Hangman. You have 6 guesses!"

     # This sets the hangman word
     secret_word = get_word()

     # This imports the hangman images
     # 6 images for 6 mistakes
     from hangman_lib import *
     
     # Other stuff for keeping a record of progress
     blanks = len(secret_word)  
     mistakes = 0
     attempts = 0
     wrong_letters= "Incorrect guesses so far: "
     past_guesses = ""
     
     while mistakes < 6:
          guess = raw_input("Guess one letter!")
          attempts = attempts + 1 
          # evaluate if letter is even acceptable
          if len(guess) > 1: 
               print "One letter at a time please!" 
          elif guess in past_guesses:
               print "You've already guessed that letter. Try again."

          # evaluate letter from here
          else:
               past_guesses = past_guesses+guess
               x = print_guessed(secret_word, past_guesses) 
               print x

               # Zero correct guesses at start
               if x.count("-") == blanks:
                    wrong_letters = wrong_letters+guess
                    mistakes = mistakes + 1

               # All correct guesses at end 
               elif x.count("-") == 0:
                    print "Omg YOU GOT IT! The mystery word was", "'"+secret_word+"'."
                    break

               # One correct guess
               else:
                    # x.count("-") < blanks:
                    mistakes = mistakes + 0
                    blanks = x.count("-")

               # Print hangman image
               print_hangman_image(mistakes)

               # Print record so far
               print "Number of attempts:", attempts
               print "Number of mistakes:", mistakes
               print wrong_letters
               print
               print 
     if mistakes >= 6:
          print "Too many mistakes :( Better luck next time!"
          print "Anyway, he secret word was", "'"+secret_word+"'."
     print "Game over."

# ----------------------End of Hangman script-----------------------
