# Valerie Lim
# Date: 15 Jan 2017
# Title: Zellers Date Algorithm

name = raw_input("Enter your first name:")

months_list = ["january", 'february', 'march', 'april', 'may',\
                'june', 'july', 'august', 'septemper', 'october',\
                'november', 'december']
while True:
    month = raw_input("Which month?")
    if all(item != str(month) for item in months_list):
        print "Month name not valid. Please check and submit again :)"
    else:
        break

date = input("Date?")
while date <= 0 or date >= 32:
    print "Please type a date that exists."
    date = input("Date?")
else:
    print "Okay!"

year = raw_input("Year?")

print "Hi", name+',', "is the date you are looking for is", month, str(date)+',', year+'?'

##### Defining values A B C D 

### Year

B = int(date)
C = int(year[-2:])
D = int(year[:2])

# print "date is", B
# print "last two digits of year are", C
# print "first two digits of year are", D

### Month

if month == "january":
    A =+ 11
    C = C - 1
elif month == "february":
    A =+ 12
    C = C - 1
elif month == "march":
    A =+ 1
elif month == "april":
    A =+ 2
elif month == "may":
    A =+ 3
elif month == "june":
    A =+ 4
elif month == "july":
    A =+ 5
elif month == "august":
    A =+ 6
elif month == "september":
    A =+ 7
elif month == "october":
    A =+ 8
elif month == "november":
    A =+ 9
elif month == "december":
    A =+ 10
else:
    A = 0

# print "month, where 1 is month starting with march, is", A
# print "new year digit", C 

##### Calculations WXYZR

W = (13*A - 1)/5
X = C / 4
Y = D / 4
Z = W + X + Y + B + C - 2*D
R = Z%7 

##### Print final result as english statement

if R == 1:
    print "That day is Monday."
elif R == 2:
    print "That day is Tuesday."
elif R == 3:
    print "That day is Wednesday."
elif R == 4:
    print "That day is Thursday."
elif R == 5:
    print "That day is Friday."
elif R == 6:
    print "That day is Saturday."
else:
    print "That day is Sunday."

    
