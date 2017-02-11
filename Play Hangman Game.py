def print_guessed(secret_word, letters_guessed):
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
     # Default = 6 chances to guess incorrectly
     print "Let's play a game of Hangman. You have 6 guesses!"
     secret_word = "abcdefgh" # for now
     blanks = len(secret_word)  # no. of possible blanks
     mistakes = 0
     past_guesses = ""
     while mistakes < 6:
          guess = raw_input("Guess one letter!")
          # evaluate if letter is even acceptable
          if len(guess) > 1: 
               print "One letter at a time please!" 
          elif guess in past_guesses:
               print "You've already guessed that letter. Try again."
          else:
               # evaluate letter from here
               past_guesses = past_guesses+guess 
               x = print_guessed(secret_word, past_guesses) 
               print x
               if x.count("-") == blanks:
                    # no correct guesses 
                    mistakes = mistakes + 1
               elif x.count("-") == 0:
                    # fully correct
                    print "Omg YOU GOT IT! The mystery word was", "'"+secret_word+"'."
                    break
               else:
                    # x.count("-") < blanks:
                    # a correct guess
                    mistakes = mistakes + 0
                    blanks = x.count("-")    # new counter
               print "Number of mistakes:", mistakes
               print "Past letters guessed:", past_guesses
               print
               print 
     if mistakes >= 6:
          print "Too many mistakes :( Better luck next time!"
          print "Anyway, he secret word was", "'"+secret_word+"'."
     print "Game over."

