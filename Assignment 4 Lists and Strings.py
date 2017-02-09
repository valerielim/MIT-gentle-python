# Name: Valerie Lim
# Date: 26 Jan, 2017, Thurs
# Title: Assignment 4 - Lists and Strings
# Notes: Taken from Lecture 2 Handouts
# Exercise 2.7 - 2.10

def sum_all(number_list):
    # number_list is a list of numbers
    total = 0
    for num in number_list:
        total += num

    return total

# Test cases
print "sum_all of [4, 3, 6] is:", sum_all([4, 3, 6])
print "sum_all of [1, 2, 3, 4] is:", sum_all([1, 2, 3, 4])



##### Exercise 2.7 - Working with lists
# This function returns the sum of
# all the cumulative elements before it.
# therefore the cumulative_sum of [4,3,6]
# is [4,7,13].

def cumulative_list(oldlist):
    # oldlist is name of list to be modified
     index = 0
     newlist = []
     while index < len(oldlist):
          if index == 0:
               new = oldlist[index]
          else: 
               new = oldlist[index] + newlist[index-1]
          newlist.append(new)
          index = index + 1
     return newlist 

# Test cases

print "The cumulative sum of [1,1,1] is", cumulative_list([1,1,1])
print "The cumulative sum of [2,4,6] is", cumulative_list([2,4,6])
print "The cumulative sum of [1,2,3] is", cumulative_list([1,2,3])



##### Exercise 2.8 - Report Card with GPA
# This prints out a report card with the overall GPA stated at the end.

classnum = input("How many classes did you take?")
output = ["REPORT CARD"]
GPA = []
counter = 0

while counter < classnum :
     classname = raw_input("What is the name of this class?")
     classgrade = input("What was your grade? (numerical form)")
     GPA.append(classgrade)        # separate list for GPA calculation
     newline = str(classname+" - "+str(classgrade))    
     output.append(newline)        # new line for each subject and grade
     counter = counter + 1
print
print "\n".join(output)
# calculate GPA
finalgpa = sum(GPA)/float(len(GPA)) 
print
print "Overall GPA: ", finalgpa
print "Not bad!"

# Note to self:
# print "\n".join(['I', 'would', 'expect', 'multiple', 'lines'])
# make this into a function find_gpa() 





##### Exercise 2.9 - Pig Latin Converter
# Converts a single word to pig latin

def pig_latin(word):          # Note: words must be input in inverted commas
     str.lower(word)
     vowels =  'aeiou'
     bonus = ["th", "st", "qu", "pl", "tr"]
     if word[0] in vowels:
          # if word starts with vowel
          output = word+"hay"
     elif word[:2] in bonus:
          # if word starts with special combo th, st, qu, etc.
          output = word[2:]+word[:2]+"ay"
     else:
          output = word[1:]+word[0]+"ay"
     return output

# Test cases

print "Boot in pig latin is", pig_latin("boot")
print "Python in pig latin is", pig_latin("python")
print "Github in pig latin is", pig_latin("github")
print "Apple in pig latin is", pig_latin("apple")





##### Exercise 2.10 - List Comprehensions

# Qn 1: Write a list comprehension that prints a list of the
# cubes of the numbers 1 through 10.

cube = [x**3 for x in range(1,11)]



# Qn 2: Write a code that prints ALL possible results of X coin flips.
# Note: print 'h' for heads, 't' for tails. So "ht" is a possible result.
# Note to self: STUCK ON THIS ONE

# This one produces some combinations of X, but not the type we want.
# results: h, t, ht, th, tt, hh

def randomcoin(flips):
     import random
     results = 0
     output = ""
     while results < flips:
          coin = random.randint(1, 2)
          if coin == 1:
               output = output+"h"
          else:
               output = output+"t"
          results = results + 1
     print output 

# This one also doesnt produce the combinations of X we want.
# Shows all combinations, but under the commutative law:
# result: h, t, ht.

import itertools

coinsides = ["h", "t"]
s = itertools.combinations(coinsides, 3)
print s

### Ok final solution time!! THIS ONE WORKS:

coin1 = ["h", "t"]
coin2 = ["h", "t"]
output = [x+y for x in coin1 for y in coin2]
print output 



# Qn 3: Write a function that takes in a string and uses a list comprehension
#to return all the vowels in the string.

def find_vowels():
     sentence = raw_input("What sentence would you like to parse?")
     vowels = ["a", "e", "i", "o", "u"]
     output = [x for x in sentence if x in vowels]
     print output 



#Qn 4: Run this list comprehension in your prompt:
     
# [x+y for x in [10,20,30] for y in [1,2,3]]

# Figure out what is going on here, and write a
# nested for loop that gives you the same result.
# Make sure what is going on makes sense to you!

x = [1,2,3]
y = [10,20,30]

output = []
for i in y:
     for j in x:
          output.append(i+j)
print output

### Note to self: expected output = [11, 12, 13, 21, 22, 23, 31, 32, 33]
# sOLVED :) 




# ---------------------

# OPTIONAL QN 1: PIG LATIN SENTENCE TRANSLATOR
# Completed; see separate doc


# ---------------------

# OPTIONAL QN 2.
 

##### Qn2.1: Write a function that takes in a list of
# elements of different types and uses a list comprehension
# to return all the elements of the list of type int.

# Note: The function isinstance will be of help here. Google “Python
# isinstance” and see if you can figure out what it does, or
# type help(isinstance) at the Python shell.

def return_int(items):
    # items is the list of items to be sorted
    # category of item returned currently set as integer.
    index = 0
    output = []
    while index < len(items):    
        if isinstance(items[index], int):
            output.append(items[index])
        index = index + 1
    return ', '.join(str(x) for x in output)    # Note to self: join function is different for integers compared to strings! 

# Test case

print "Sample list 'Messy' contains [[1,2,3], 100, 'apples', 3.333]."
print "The output for return_int(messy) that returns only integers is", return_int(messy)



##### Qn2.2: Write a function that solves Y = X**2 + 1
# for the domain x = -5 to 5, and y = 0 to 10.
# Your solution should print out a list of [x, y] pairs.


### Working notes
# y = x**2 + 1
# x in range -5 to 5

# x = (y-1)**0.5
# y in range 0 to 10

# Extra: As a function that solves y = x**2 + 1

def solve_eqn(y):
     output = float((y-1)**0.5)
     return output 

# As a list comprehension:

varX = [float((x-1)**0.5) for x in range(1, 11)]
varY = [float((y)**2+1) for y in range(-5, 6)] 

# Note: testY calculates the value of Y. where X = -5 to 5.
# Format: [x, y]

counterX = [a for a in range(-5, 6)]
testY = [[a, y] for a, y in zip(counterX, varY)]

# Note: testX calculates the value of X. where Y = 0 to 10.
# Format: [x, y]

counterY = [b for b in range(0, 11)]
testX = [[x, b] for x, b in zip(varX, counterY)]

# Bonus: To print the list comprehensions NICELY because
# I truly HATE seeing them as a clump:

def present_nicely(item):
     # item is the name of the list comprehension
     index = 0
     while index < len(item):
          print item[index]
          index = index + 1
