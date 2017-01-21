# Valerie Lim
# Title: Homework 1 Hello World.py
# Date: Jan 10, 2016
# Lecture 1, Homework 1, Qn 1.1 - 1.8

##### Exercise 1.1 - 1.3
# prints "Hello, World!" to the screen
print "Hello, world!"

# prints tictactoe board
print "  |  |   "
print "---------"
print "  |  |   "
print "---------"
print "  |  |   "



##### Exercise 1.4
# Print the following equations without simplyifying them.
# Save each value as a variabe, then print the variable.

qn1 = (3*5)/(2+3)
qn2 = math.sqrt(7+9)*2
qn3 = (4-7)**3
qn4 = (-19+100)**(1/4.0)



##### Exercise 1.5 

# name = raw_input("What is your name? ")
# city = raw_input("What city do you live in? ")
# state = raw_input("What state is that in? ")
# print "Hello there! It is so great to meet you,"
# print name, "from", city, state

###Age expression

age = raw_input("Pardon my rudeness, but how old are you? ")
print  "Wow! You look like you could be", int(age)-int(age)*0.15, "!!"


 
##### Exercise 1.7 Rock Paper Scissors

print "Hi there! This is a game of rock paper scissors lizard spock. Please spell the item correctly or you will be scolded. Have fun!"
print " "
print "Your options are:"
print "rock"
print "scissors"
print "paper"
print " "
player1 = raw_input("Player 1?")
player2 = raw_input("Player 2?")

### Options are strictly 
# rock
# paper
# scissors
# All other rules apply as normal. 

### All combinations of rock
    
if player1 == "rock":
    if player2 == "rock":
        print "The players tie."
    elif player2 == "scissors":
        print "Player 1 wins. Rock crushes scissors."
    elif player2 == "paper":
        print "Player 2 wins. Paper wraps the rock up."
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
    else:
        print "YOU TYPED SOMETHING WRONG NOOBSHIT"


        
##### Exercise 1.8 Qn 1
# Using a for loop, write a program that
# prints out the decimal equivalents of
# 1/2, 1/3, 1/4 ... 1/10. 

denominator = 1.00
for i in range(1, 10, 1):
    print denominator/i


    
##### Exercise 1.8 Qn 2
# Write a program using a while loop that asks the user
# for a number, and prints a countdown from that number
# to zero. 

print "This function will ask the user for a number, and\
will print a countdown from that number to zero."
print " "

num = input("Gimme a number. Make sure its a whole number ok.")

if num < 0:
    print "Please do not provide a negative integer. This means your number has to be larger than or equal to 0."
    num = input("Let's try again. Gimme a number. Make sure its a whole number ok. And positive too :)")    

while num >= 0:
    print num  
    num = num - 1



##### Exercise 1.8 Qn 3

# base = input("what would you like the base number to be?")
# exp = input("what would you like the exponent to be?")

print int(base**exp)



##### Exercise 1.8 Qn 4 

# Write a program using a while loop that asks the user to enter
# a number that is divisble by 2. Give the user a witty mssage if they
# enter something that is not divisble by 2 -- and make them enter a new
# number. Don't let them stop until they enter an even number! Print a
# congratulatory message when they *finally* get it right. 

number = input("Please enter a number divisble by 2.")
while number%2 != 0:
    print "That's not divisible by 2. Could you try again?"
    print "... Noobshit."
    number = input("Please enter a number divisble by 2.")
else:
    print "Thank you! Finally. What a relief. You are very helpful."

    

