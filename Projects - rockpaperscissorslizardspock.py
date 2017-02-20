# Valerie Lim
# Date: 15 Jan 2017
# Title: rockpaperscissorslizardspock.py

##### This is will compute which of 2 players is the winner
##### in a game of rock paper scissors spock lizard. 

### Options are strictly 
# rock
# paper
# scissors
# spock
# lizard

### additional rules
# spock smashes rock and scissors.
# spock is disproved by paper.
# spock is also scared of lizards.
# lizard shits on paper.
# lizard scares spock.
# lizard is harmed by rock and scissors.

# All other rules apply as normal. 

##### Begin

print "Hi there! This is a game of rock paper scissors lizard spock. Please spell the item correctly or you will be scolded. Have fun!"
print " "
print "Your options are:"
print "rock"
print "scissors"
print "paper"
print "spock"
print "lizard"
print " "
player1 = raw_input("Player 1?")
player2 = raw_input("Player 2?")

### All combinations of rock
    
if player1 == "rock":
    if player2 == "rock":
        print "The players tie."
    elif player2 == "scissors":
        print "Player 1 wins. Rock crushes scissors."
    elif player2 == "paper":
        print "Player 2 wins. Paper wraps the rock up."
    elif player2 == "lizard":
        print "Player 1 wins. Rock crushes the lizard. Gross."
    elif player2 == "spock":
        print "Player 2 wins. Spock explodes rock with laser eyes."
    else:
        print "YOU TYPED SOMETHING WRONG NOOBSHIT"

### All combinations of scissors

if player1 == "scissors":
    if player2 == "rock":
        print "Player 2 wins. Rock crushes scissors."
    elif player2 == "scissors":
        print "The players tie."
    elif player2 == "paper":
        print "Player 1 wins. Scissors cuts the paper up."
    elif player2 == "lizard":
        print "Player 1 wins. Scissors stabs the lizard. It dies."
    elif player2 == "spock":
        print "Player 2 wins. Spock desctroys scissors with epic vulcan powers."

    else:
        print "YOU TYPED SOMETHING WRONG NOOBSHIT"

### All combinations of paper
        
if player1 == "paper":
    if player2 == "rock":
        print "Player 1 wins. Paper wraps the rock up."
    elif player2 == "scissors":
        print "Player 2 wins. Scissors cuts the paper up."
    elif player2 == "paper":
        print "The players tie."
    elif player2 == "lizard":
        print "Player 2 wins. Lizard shits on paper."
    elif player2 == "spock":
        print "Player 1 wins. Paper disproves Spock. Spock sad."
    else:
        print "YOU TYPED SOMETHING WRONG NOOBSHIT"

### Spock easter egg

if player1 == "spock":
    if player2 == "rock":
        print "Player 1 wins. Spock explodes rock with laser eyes."
    elif player2 == "scissors":
        print "Player 1 wins. Spock desctroys scissors with epic vulcan powers."
    elif player2 == "paper":
        print "Player 2 wins. Paper disproves Spock. Spock sad."
    elif player2 == "lizard":
        print "Player 2 wins. Spock is scared of lizards."
    elif player2 == "spock":
        print "The players tie."
    else:
        print "YOU TYPED SOMETHING WRONG NOOBSHIT"

if player1 == "lizard":
    if player2 == "rock":
        print "Player 2 wins. Rock crushes the lizard. Gross."
    elif player2 == "scissors":
        print "Player 2 wins. Scissors stabs the lizard. It dies."
    elif player2 == "paper":
        print "Player 1 wins. Lizard shits on paper."
    elif player2 == "spock":
        print "Player 1 wins. Spock is scared of lizards."
    elif player2 == "lizard":
        print "The players tie."
    else:
        print "YOU TYPED SOMETHING WRONG NOOBSHIT"

