# Valerie Lim
# 2 March 2017
# Class exercise 6, from readings

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
