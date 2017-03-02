# Valerie Lim
# 2 March 2017
# Class exercise 6

# ------- Chapter 12 -------

##### Write a function that calculates the distance between two points
     
class point:
     pass

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
     print "Time is", str(time.hours)+":"+str(time.minutes)+":"+str(time.seconds)+"."

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

# Converts time in hh:mm:ss into purely seconds
def convertToSeconds(t):
  minutes = t.hours * 60 + t.minutes
  seconds = minutes * 60 + t.seconds
  return seconds

# Converts seconds back into time format, hh:mm:ss
def makeTime(seconds):
  time = Time()
  time.hours = seconds // 3600
  time.minutes = (seconds%3600) // 60
  time.seconds = seconds%60
  return time

# adds two times (eg. 1.5hr and 0:43:30) together
def addTime(t1, t2):
  seconds = convertToSeconds(t1) + convertToSeconds(t2)
  return makeTime(seconds)

# Increments a given time by (x) seconds

def increment(time, seconds): 
     time = convertToSeconds(time)
     newtime = time + seconds
     return makeTime(newtime)
