# -*- coding: cp1252 -*-
# Valerie Lim 
# Date: Jan 11, 2016
# Lecture 1, Written Exercise - Conditionals Testing
# Title: Class Exercise 1 

##### Exercise 1.9: Legal names

# 1. and is a legal
# 2. _and is NOT legal because it starts with the illegal character (_)
# 3. var is legal
# 4. var1 is legal
# 5. 1var is NOT legal because names cannot start with numbers
# 6. my-name is NOT legal because it uses (-)
# 7. your-name is legal
# 8. COLOR is legal



##### Exercise 1.10: Types

# 1. boolean
# 2. float
# 3. string
# 4. integer
# 5. string
# 6. integer
# 7. string
# 8. boolean
# 9. string



##### Exercise 1.11 is a drawing (on paper) exercise

##### Exercise 1.12: Boolean operators

# 1. FALSE
# 2. TRUE
# 3. TRUE
# 4. TRUE
# 5. FALSE


##### Exercise 1.13: Conditionals

### Note
# The original code (below) does not seem to work properly.
# Made some edits (second part).

# pay = _____
# location = _____
# if location == "U.S.S. Enterprise":"
# print "So long, suckers! I’ll take it!"
# elif location == "Massachusetts":
# if pay < 100000:
# print "No way"
# else:
# print "I’ll take it!"
# elif location == "California" and pay > 40000:
# print "I’ll take it!"
# elif pay > 60000:
# print "I’ll take it!"
# else:
# print "No thanks, I can find something better."

### Edited code

pay = raw_input("Pay?")
location = raw_input("Location?")

if location == "U.S.S. Enterprise":
    print "So long, suckers! I’ll take it!"
elif location == "Massachusetts":
    if int(pay) < 100000:       
        print "No way"
    else:
        print "I’ll take it!"
elif location == "California" and int(pay) >40000:
    print "I’ll take it!"
else:
    print "No thanks, I can find something better."


##### Exercise 1.14: Understanding loops

# Question 1

num = 10
while num > 3:
    print num
    num = num - 1

# result 10 9 8 7 6 5 4 
# Question 2

divisor = 2
for i in range(0, 10, 2):
    print i/divisor

# note to self - range = 0 - 10, with increments of 2. 
# Result: 0 1 2 3 4

for i in range(0, 10, 2): 
    print i

# Question 3

num = 10
while True:
    if num < 7:
        break
    print num
    num -= 1

# result: 10 9 8 7
# Continue until num is <7, aka 6.

# Question 4


count = 0
for letter in "Snow!":
    print "Letter #", count, "is", letter
    count += 1

# Prints repeatedly, "Letter # 0 is S" / "Letter # 1 is N" etc
# Was going to cycle through all letters anyway
# Count += 1 command just increases the count at the same time.



#####Exercise 1.15: Buggy loop (Find the bug!)

# Part 1 - Values
# Values of i : 10, 5, 6, 3, 4, 2, 1, 2, 1, 2, 1, ... etc
# Values of n : 10, 10, 10... etc

# Part 2 - debugging
# Firstly, it's hard to tell what Ben is doing with the variable n.
# I am guessing that "n = 10" may have meant that the number of\
# loops is intended to be 10. Or, he e may have wanted to find
# the 10th result.

# Next, it seems like Ben wants to take i and /2 if
# it is an even number, or +1 if it is odd. He wants to do this while
# i > 0 and the loop is expected to stop if the value of i falls below
# 0. Ben has stated that i = 10 at the start. 

# There is a problem with this loop as (based on the answer in P1)
# the value of i does not ever fall below 0. This means the loop will
# repeat forever. This is not good.

# One solution is to set the condition for the while loop as i <= 1,
# which would stop the loop before it repeats infinitely.

# Another solution is to change the "else" condition from (i = i + 1)
# to (i = i - 1), which would bring the result closer to zero in a
# similar pattern. 

# Finally, if he meant to print n=10 results, he could write the code as such

# n = 10
# i = 10

# for n in range(10):
#   while i > 0:

