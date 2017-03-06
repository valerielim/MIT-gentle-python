# Valerie Lim
# 2 March 2017
# Completed: 6 March 2017
# Class exercise 6

# ------- Chapter 12 -------

##### Write a function that calculates the distance between two points
     
class point:
     def __init__(self, x=0, y=0):
          self.x = x
          self.y = y

     def __str__(self):
          return "(" + str(self.x) + "," + str(self.y) + ")"
          
     def __add__(self, other):
          return point(self.x + other.x, self.y + other.y)

     def __sub__(self, other):
          return point(self.x - other.x, self.y - other.y)

place1 = point()
place1.x = 0
place1.y = 0

place2 = point()
place2.x = 0
place2.y = 0

def distance(point1, point2):
     import math
     distance = math.sqrt((point1.x - point2.x)**2 \
                          + (point1.y - point2.y)**2)
     return distance 
     
##### Write a function that moves a rectangle by 2 parameters dx, dy

class rectangle:
     pass

baikoh = rectangle()
baikoh.corner = point()
baikoh.corner.x = 10.0
baikoh.corner.y = 20.0

def moverect(rect, dx, dy):
     print "The old coordinates were", '('+str(rect.corner.x)+',', str(rect.corner.y)+')'
     rect.corner.x = rect.corner.x + dx
     rect.corner.y = rect.corner.y + dy
     print "The new coordinates are", '('+str(rect.corner.x)+',', str(rect.corner.y)+')'

##### Write a function that creates a new rectangle, then moves it by 2 parameters, dx, dy.
##### You may use code from the previous exercise.

def moveNewrect(rect, dx, dy):
     print "The old coordinates were", '('+str(rect.corner.x)+',', str(rect.corner.y)+')'
     import copy
     newbox = copy.deepcopy(rect)
     newbox.corner.x = rect.corner.x + dx
     newbox.corner.y = rect.corner.y + dy
     print "The new coordinates are", '('+str(newbox.corner.x)+',', str(newbox.corner.y)+')'     

# ------- Chapter 13 -------

# test cases
class time:
     pass

time1 = time()
time1.hours = 11
time1.minutes = 59
time1.seconds = 30

time2 = time()
time2.hours = 14
time2.minutes = 20
time2.seconds = 41

time3 = time()
time3.hours = 14
time3.minutes = 20
time3.seconds = 42

# Print time from class
def printTime(time):
     print str(time.hours)+":"+str(time.minutes)+":"+str(time.seconds)

# Function returns if T2 occurs after T1
def after(t1, t2):
     print "Time is", str(t1.hours)+":"+str(t1.minutes)+":"+str(t1.seconds), "and", str(t2.hours)+":"+str(t2.minutes)+":"+str(t2.seconds)+"."
     print "T2 occurs after T1:"
     if t1.hours < t2.hours:
          return True
     elif t1.hours > t2.hours:
          return False
     else:
          if t1.minutes < t2.minutes:
               return True
          elif t1.minutes > t2.minutes:
               return False
          else:
               if t1.seconds > t2.seconds:
                    return False
               elif t1.seconds < t2.seconds:
                    return True
               else:
                    print "T1 and T2 are the same time."

# Converts Time object (eg. time1) into purely seconds
def convertToSeconds(t):
  minutes = t.hours * 60 + t.minutes
  seconds = minutes * 60 + t.seconds
  return seconds

# Converts xxx seconds back into time format, hh:mm:ss
def makeTime(seconds):
  time = time()
  time.hours = seconds // 3600
  time.minutes = (seconds%3600) // 60
  time.seconds = seconds%60
  return time

# adds two times together
def addTime(t1, t2):
  seconds = convertToSeconds(t1) + convertToSeconds(t2)
  return makeTime(seconds)

# Increments a given time by (x) seconds
def increment(time, seconds): 
     time = convertToSeconds(time)
     newtime = time + seconds
     return makeTime(newtime)

# ------- Chapter 14 -------

# makes "converttoseconds" function from section 13.5 to a method
# in the Time class.

# Note: class "Time14" is a new class just for messing around stuff in
# chapter 14! Even though it has same attributes as class "time".

class Time14:
     def __init__(self, hours=0, minutes = 0, seconds=0):
          self.hours = hours
          self.minutes = minutes
          self.seconds = seconds
          
     def printTime(time):
          print str(time.hours) + ":" +  \
               str(time.minutes) + ":" +  \
               str(time.seconds)

     def convertToSeconds(self):
          minutes = self.hours * 60 + self.minutes
          seconds = minutes * 60 + self.seconds
          return seconds

     def increment(self, seconds):
          self.seconds = seconds + self.seconds
          while self.seconds >= 60: 
               self.seconds = self.seconds - 60 
               self.minutes = self.minutes + 1 
          while self.minutes >= 60: 
               self.minutes = self.minutes - 60 
               self.hours = self.hours + 1
          return printTime(self)

     # function "after" takes 2 times, prints answer if
     # one time is less than/comes before the other.

     # E.g., t1 = 10:00:00
     # E.g., t2 = 10:00:01
     # It will print "the bread is done" if t2 > t1.
     
     def after(self, time2):
          if self.hours > time2.hours:
                result = 1
          elif self.hours < time2.hours:
               result = 0
          else:
               if self.minutes > time2.minutes:
                    result = 1
               elif self.minutes < time2.minutes:
                    result = 0
               else:
                    if self.seconds > time2.seconds:
                         result = 1
                    else:
                         result = 0
          if result == 0:
               print "The bread is done."
          else:
               print "The bread is not done yet."

# Test case

currentTime = Time14()
currentTime.hours = 17
currentTime.minutes = 23
currentTime.seconds = 01

doneTime = Time14()
doneTime.hours = 17
doneTime.minutes = 23
doneTime.seconds = 03

# Ex 14.5
# Qn: "Add a fourth parameter to the "FIND" function,
# that specifies where to stop looking.

#### PS: The defaultvalue of 'end' should be len(str),
# but that won't work here. This is because the default
# values are evaluated when the function is defined, not
# when it is called. When FIND is defined, 'str' doesn't
# exist yet, so you can't find its length.)

#### PPS: To me, I interpret this as two requirements:
#    1. To let the user define their own end
#    2. If their end is not specified, default to searching whole word


def find(str, ch, start=0, end=0):
     index = start
     if end == 0:
          end = end + len(str)
     elif end > len(str):
          print "Invalid end position defined." 
     else:
          end = end
     while index < end: 
          if str[index] == ch: 
               return index 
          index = index + 1 
     return -1    # aka, "not found"

# Ex 14.6
# Create a new operator "subtraction" or "sub"
# that overloads the subtraction operator, and try it out.

class Point:
     def __init__(self, x=0, y=0):
          self.x = x
          self.y = y

     def __str__(self):
          return "(" + str(self.x) + "," + str(self.y) + ")"
          
     def __add__(self, other):
          return point(self.x + other.x, self.y + other.y)

     def __sub__(self, other):
          return point(self.x - other.x, self.y - other.y)

     def __rmul__(self, other):
          return point(other * self.x, other * self.y)
     
p1 = Point(1,1)
p2 = Point(2,2)
p3 = Point(3,5)

