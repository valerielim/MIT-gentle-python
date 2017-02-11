# Name: Valerie Lim
# Date completed: 6 Feb 2017, Monday
# Title: Pig Latin Translator

##### Pig Latin Translator

# This code will ask for a phrase you would like to convert.
# It will then print the translation in pig latin.
# It will not change or remove punctuation.
# It will not change or remove numbers present.
# It works for contractions too - I'm, can't, they're etc.


# Function for converting a single word:

def pig_latin(word):          # words must be input in inverted commas
     str.lower(word)
     vowels =  'aeiou'
     bonus = ["th", "st", "qu", "pl", "tr"]
     if word[0] in vowels:
          # word starts with vowel
          output = word+"hay"
     elif word[:2] in bonus:
          # word starts with special combo th, st, qu, etc.
          output = word[2:]+word[:2]+"ay"
     else:
          # All other words starting with a consonant
          output = word[1:]+word[0]+"ay"
     return output

# Function for converting full sentence(s):

def pig_latin_full():
     phrase = raw_input("What phrase would you like to convert to pig latin?")
     import re                               # This segments each word AND punctuation into elements of a list
     sentence = re.findall(r"[\w']+|[.,!?;:]", phrase)
     print sentence
     holder = ""
     index = 0
     while index < len(sentence):
          word = sentence[index]             # Individual word
          if word.isalpha():
               newword = pig_latin(word)     # Note: pig_latin(word) comes bk as STRING
               holder = holder+newword+" "
               index = index + 1
          else:
               # for punctuation, numbers, symbols
               # No change
               newword = word           
               index = index + 1          
               holder = holder[:-1]+newword+" "
     print phrase, "translates to", holder, "in Pig Latin."

