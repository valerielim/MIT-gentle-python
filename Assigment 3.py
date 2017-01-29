# Valerie Lim
# Date: 21 Jan 2017, Saturday
# Title: Assignment 3
# Notes: Question sheet from Handouts on Lecture 2.
# Exercise 2.0 - 2.4

# Other notes: ITS RAINING AND FREAKING COLD TODAY

##### Exercise 2.0

def f1(x):
    print x + 1

def f2(x):
    return x + 1

# Difference between print and return: In f1, the function does
# not return a value, so so there's nothing to add to 1. This
# generates an error.

# In f2, the function returns a value (4), so there's something
# to add to 1. In this case 4+1=5.



##### Exercise 2.1

# Use your rock paper scissors code from Assignment 1
# Rephrase it in terms of parameters rather than asking the user
# directly for an input.
# Also include at least 3 test cases below. 

# RPS = Rock Paper Scissors

def RPS(player1, player2):
    if player1 == "rock":
        if player2 == "rock":
            print "The players tie."
        elif player2 == "scissors":
            print "Player 1 wins. Rock crushes scissors."
        elif player2 == "paper":
            print "Player 2 wins. Paper wraps the rock up."
        else:
            print "YOU TYPED SOMETHING WRONG NOOBSHIT"
    if player1 == "scissors":
        if player2 == "rock":
            print "Player 2 wins. Rock crushes scissors."
        elif player2 == "scissors":
            print "The players tie."
        elif player2 == "paper":
            print "Player 1 wins. Scissors cuts the paper up."
        else:
            print "YOU TYPED SOMETHING WRONG NOOBSHIT"
    if player1 == "paper":
        if player2 == "rock":
            print "Player 1 wins. Paper wraps the rock up."
        elif player2 == "scissors":
            print "Player 2 wins. Scissors cuts the paper up."
        elif player2 == "paper":
            print "The players tie."
        else:
            print "YOU TYPED SOMETHING WRONG NOOBSHIT"

# Note: unsolved problem that input has to include inverted commas
# or else code cannot recognise input. eg. RPS("rock", "rock").



##### Exercise 2.2.1
# Define is_divisible function here

def is_divisible(m, n):
    if n == 0 :
        return "The value of n cannot be zero."
    elif m%n == 0:
        return True
    else: 
        return False

# Test cases for is_divisible function

print is_divisible(10, 5)  # This should return True
print is_divisible(18, 7)  # This should return False
print is_divisible(42, 0)  # What should this return? Ans: ERROR



##### Exercise 2.2.2
# Create a function that replaces != and title it not_equal

def not_equal(j, k):
    if j == k:
        return "They are equal."
    else:
        return "They are not equal."

# Test cases for not_equal function

print not_equal(1, 1)               # Equal
print not_equal("1", 1)             # Not equal, because different types
print not_equal(1, "one")           # Not equal, because different types
print not_equal("apple", "apple")   # Equal
print not_equal(1+1, 1+2)           # Not equal, mathematically



##### Exercise 2.3.0
# Write a function that converts degrees to radians

def radians(n):
    import math
    rad = (n/360.00)*2*math.pi
    return rad

# Test cases for radians

print radians(90)       # 1.57079632679 radians
print radians(180)      # 3.14159265359 radians aka pi
print radians(91)       # 1.58824961931 radians
print radians(360)      # 6.28318530718 radians aka 2 pi



###### Exercise 2.3.1
# Write a function multadd that takes 3 parameters, a, b and c.
# Combine them as such: a*b+c

def multadd(a, b, c):
    return a * b + c

# Test cases for multadd function

print multadd(1, 2, 3)      # The result should be 5
print multadd(3, 2, 1)      # The result should be 7
print multadd(1, 3, 2)      # The result should be 5



##### Exercise 2.3.2.1
# Print out the following equation using the multadd function 

angle_test = multadd(0.50, math.cos(math.pi/4), math.sin(math.pi/4))
return angle_test            # The answer should be 1.06066017178



##### Exercise 2.3.2.2
# Print out the following equation using the multadd function 

ceiling_test = multadd(2, math.log(12, 7), math.ceil(276/19.00))
return ceiling_test          # The answer should be 17.5539788165 



##### Exercise 2.3.3

def yikes(x):
    a = x
    b = math.exp(-x)
    c = (1-math.exp(-x))**0.5
    return multadd(a, b, c)

# Answer for yikes(5) should be 1.0303150673048738



##### Exercise 2.4.1

import math
import random

def rand_divis_3():
    x = random.randint(0,100)
    print "x is", x
    if x%3 == 0:
        return "True"
    else:
        return "False"

    

##### Exercise 2.4.2
# Write a function that takes in 2 parameters: the number of dice,
# and the number of sides of each dice. Then, generates a random roll
# values for each die rolled. Print out each roll then return the
# string with "That's all!"

def roll_dice(a, b):
    # a is number of sides of each die
    # b is number of dice to roll
    # assume each dice has a minimum of 1 side
    # assumes all dice has same number of sides
    i = 1
    while i <= b:
        x = random.randint(1, a)
        print x
        i = i + 1
    print "That's all!", b, "dice right?"



##### Exercise 2.5 Quadratic Formulas
# Write a function "roots" that computes the roots of a quadratic
# equation. Check for complex roots and print an error message saying
# if the roots are complex. 

print "To use this, type 'roots(a,b,c)' with the values of a, b and c \
following the formula below:"
print "The formula is ax**2 + bx + c."
print
print "Note: this function can only calculate real roots and not complex roots."
print
print "Go!"

# a = input("What is the coefficient of x squared?")
# b = input("What is the coefficient of x?")
# c = input("What is the remaining values to be added?")

def roots(a, b, c):
    import math
    int(a)
    int(b)
    int(c)
    if (b**2 - 4*a*c) < 0:
        return "Error: the roots are complex."
    else:
        # For root 1 and root 2
        root1 = (-b + math.sqrt(b**2-4*a*c))/2
        root2 = (-b - math.sqrt(b**2-4*a*c))/2
        print "The roots of this quadratic equation are", root1, "and", str(root2)+"."

# Test cases for Roots function

# roots(1,-2,-3) should return roots -1.0, 3.0.
# roots(1,-6,9) should return roots 3.0 only.
# roots(1,3,3) should return an error. No real roots.

