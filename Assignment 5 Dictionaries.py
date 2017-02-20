# Valerie Lim
# Date started: 16/2/2017
# CompleteD: 20/2/2017
# Title: Assignment 5 Dictionaries
# Source: Homework 3, Lecture 5. 

# Exercise 3.1 - Additional List Practice

# sample lists
a = [1,3,5]
b = [5,3,1]

c = [1,3,6,9]
d = [10,14,3,72,9]

e = [2,4,6]
f = [1,3,5]

g = [2,3]
h = [3,3,3,2,10]

def list_intersection(lista, listb):
     # this function returns the intersection of two lists
     # a and b are the names of lists to be compared
     output = []
     for i in lista:
          if i in listb:
               if i not in output:
                    output.append(i)
     return output 

# Test cases
# print "The intersection of list a, b is:", list_intersection(a,b)
# print "The intersection of list c, d is:", list_intersection(c,d)
# print "The intersection of list e, f is:", list_intersection(e,f)
# print "The intersection of list g, h is:", list_intersection(g,h)





##### Exercise 3.2 - Collision Detection of Balls

# PLAN
# 1: compute distance between center of balls in (x, y)
# 2: compute sum of their radii
# 3: if distance in (1) is less than (2) = they are coliding [true]

def colliding_balls(a, b):
     # function will identify if space is 2D or 3D based on coordinates provided
     # format
     # a has coordinates [r, x1, y1, z1]
     # b has coordinates [r, x2, y2, z2]
     while len(a) != len(b):
          print "Vector inputs of ball coordinates are not compatible (e.g., 2D and 3D)"
          break
     while len(a) == len(b):
          # 3D space
          if len(a) == 3:
               distance = float(((b[1]-a[1])**2 + (b[2]-a[2])**2 + (b[3]-a[3])**2)**0.5)
               
          # 2D space
          else:
               distance = float(((b[1]-a[1])**2 + (b[2]-a[2])**2)**0.50)
               
          sumrad = int(a[0])+int(b[0])
          if distance - sumrad > 0:
               print "False. They are not colliding"
               break
          else:
               print "True. They are colliding."
               break

# Test cases for 2D
AA = [1,1,1]
BB = [3,5,1]

XX = [3,5,9]
YY = [3,4,9]

# Test cases for 3D
AAA = [1,1,1,1]
BBB = [3,5,1,9]

XXX = [3,5,2,9]
YYY = [3,4,2,9]



##### Exercise 3.3 - Intro to dictionaries

# Create a dictionary for all the modules you've taken

Psychmods = {'PL1101' : 'Intro to Psych', 'PL4225' : 'Therapies'}





##### Exercise 3.4 - More about Dictionaries

NAMES = ["Alice", "Bob", "Cathy", "Dan", "Ed", "Frank",
"Gary", "Helen", "Irene", "Jack", "Kelly", "Larry"]

AGES = [20, 21, 18, 18, 19, 20, 20, 19, 19, 19, 22, 19]

def combine_lists(lista, listb):
     dictionary = {}
     index = 0
     while index < len(lista):
          dictionary[lista[index]] = listb[index]
          index = index + 1
     return dictionary
     
def people(age):
     dic = combine_lists(NAMES, AGES)
     output = []
     for key, value in dic.iteritems():
          if int(value) == int(age):
               output.append(key)
     return output





##### 3.5 - Zeller's Algorithm
# Revised from original project
# Wrapped in function
# Uses dictionary for month function as instructed 

def zellers(month, date, year):
    # Note: month must be put in " "

    # Check for validity of input
    month = str.lower(month)
    months_list = ["january", 'february', 'march', 'april', 'may',\
                'june', 'july', 'august', 'septemper', 'october',\
                'november', 'december']
    if month not in months_list:
        print "Month name not valid. Please check and submit again :)"
        # break
    if date <= 0 or date >= 32:
        print "Please type a date that exists."
        # break
          
    # print "Hi there, the day of the date returned will be for", month, str(date)+',', str(year)+'.'
    # print "..."


    ##### Calculation
    ### Year
    C = str(year)[-2:]
    D = str(year)[:2]

    C = int(C)
    D = int(D)
    
    ### Month

    if month == "january": 
        C = C - 1
    elif month == "february":
        C = C - 1
    else:
        C = C
        # basically, do nothing
        
    dict = {}
    dict["january"] = 11
    dict["february"] = 12
    dict["march"] = 1
    dict["april"] = 2
    dict["may"] = 3
    dict["june"] = 4
    dict["july"] = 5
    dict["august"] = 6
    dict["september"] = 7
    dict["october"] = 8
    dict["november"] = 9
    dict["december"] = 10

    A = dict[month]

    ### Date
    B = int(date)
    
    ### Checks
    
    # print "Month is", A
    # print "Date is", B 
    # print "Year is", C
    # print "first two digits of year is", D

    ##### Calculations WXYZR

    W = (13*A - 1)/5
    X = C / 4
    Y = D / 4
    Z = W + X + Y + B + C - 2*D
    R = Z%7 

    ##### Print final result as english statement

    if R == 1:
        return "Monday"
    elif R == 2:
        return "Tuesday"
    elif R == 3:
        return "Wednesday"
    elif R == 4:
        return "Thursday"
    elif R == 5:
        return "Friday"
    elif R == 6:
        return "Saturday"
    else:
        return "Sunday"
