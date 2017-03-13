# Valerie Lim
# 11 March 2017
# Homework 8 -- Ex 4.3.1
# Title: tetrominoes.py

from graphics import *


# ----------- Example -----------
# what a single perfect block should look like:
def block():
    win = GraphWin("Tetrominoes", 150, 150)
    block = Rectangle(Point(30, 30), Point(60, 60))
    block.setFill("red")
    block.draw(win)

# ----------- Homework -----------

class Block(Rectangle):
    def __init__(self, point_location, colour):
        # converts x, y to display pixels
        # Grid of 30x30 pixels per block
        X0 = point_location.getX() *30
        Y0 = point_location.getY() *30
        X1 = X0 + 29
        Y1 = Y0 + 29
        self.block = Rectangle(Point(X0, Y0), Point(X1, Y1))
        self.block.setFill(colour)

    def draw(self, win): 
        self.block.draw(win) 

def Block_test():
    win = GraphWin("Tetrominoes", 150, 150)
    block1 = Block(Point(1, 1), "red")
    block2 = Block(Point(1, 2), "red")
    block1.draw(win)
    block2.draw(win)
    win.mainloop()

class Shape(Block):
    def __init__(self, point_location_list, colour):
        self.blockList = []
        for i in point_location_list:
            self.blockList.append(Block(i, colour))
            # having problems with this line
            # cannot index the self.block part
            
    def draw(self, win):
        for myBlock in self.blockList:
            myBlock.draw(win)

            
# [Given syntax]
class I_shape(Shape):
    def __init__(self, center):
        coords = [Point(center.x - 2, center.y),
            Point(center.x - 1, center.y),
            Point(center.x , center.y),
            Point(center.x + 1, center.y)]
        Shape.__init__(self, coords, "blue")

# To create a 4-cube-shaped tetromino, call this: 
win = GraphWin("Tetrominoes", 200, 150)
shape = I_shape(Point(3, 1))
shape.draw(win)
win.mainloop()

