# Valerie Lim
# Date: 10 March 2017
# Homework 8 - Graphics and Classes

# Exercise 4.1 ONLY --
#       makes a circle
#       makes a tire
#       makes a square
#       makes the tire move 100 units right

from graphics import *

def sample():

    # this creates a window, 100 x 100
    win = GraphWin("My Circle", 100, 100)

    # this creates the circle, syntax:
    # Circle(centerPoint, radius)

    # Need to create a Point for the center. Syntax:
    # Point(x, y) 
    c = Circle(Point(50,50), 10)

    # This draws the object onto a window background.
    # Needs both object AND window to be defined. Syntax:
    # object.draw(GraphWin object) 
    c.draw(win)

    # GetMouse will pause for the user to click in window
    # GetMouse returns the coordinates of where the mouse was clicked
    win.getMouse() # pause for click in window
    win.close()

# To execute, un-comment this
# sample()

def square1():

    win = GraphWin("My Square", 500, 500)
    square = Rectangle(Point(100,100), Point(400,400))
    square.setFill("Red")
    square.draw(win)
    win.getMouse() 
    win.close()

# To execute, un-comment this
# square1() 

class Wheel():

    def __init__(self, center, wheel_radius, tire_radius):
        self.tire_circle = Circle(center, tire_radius)
        self.wheel_circle = Circle(center, wheel_radius)

    def draw(self, win): 
        self.tire_circle.draw(win) 
        self.wheel_circle.draw(win) 

    def move(self, dx, dy): 
        self.tire_circle.move(dx, dy) 
        self.wheel_circle.move(dx, dy)

    def set_color(self, wheel_color, tire_color):
        self.tire_circle.setFill(tire_color) 
        self.wheel_circle.setFill(wheel_color)

    def undraw(self): 
        self.tire_circle .undraw() 
        self.wheel_circle .undraw() 

    def get_size(self):
        return self.tire_circle.getRadius()

    def get_center(self):
        return self.tire_circle.getCenter()

    def animate(self, win, dx, dy, n):
        if n > 0:
            self.move(dx, dy)
            win.after(100, self.animate, win, dx, dy, n-1)

def main():
    # create a window with width = 700 and height = 500
    new_win = GraphWin('Wheel', 700, 500) 

    # What we'll need for the wheel...
    wheel_center = Point(200, 200) # The wheel center is a Point at (200, 200)
    tire_radius = 100  # The radius of the outer tire is 100

    # Make a wheel object
    new_wheel = Wheel(wheel_center, 0.6*tire_radius, tire_radius)

    # Set its color
    new_wheel.set_color('yellow', 'orange')

    # And finally, draw it 
    new_wheel.draw(new_win)

    # Move the wheel
    new_wheel.animate(new_win, 10, 0, 100)

    # Run the window loop (must be the *last* line in your code)
    new_win.mainloop()

# Comment this call to main() when you import this code into
#  your car.py file - otherwise the Wheel will pop up when you
#  try to run your car code.

# main()

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


# To test create a 4-cube-shaped tetromino, uncomment this: 
# win = GraphWin("Tetrominoes", 200, 150)
# shape = R_shape(Point(3, 1))
# shape.draw(win)
# win.mainloop()

# Other Tetromino Shapes
class J_shape(Shape):
    def __init__(self, center):
        coords = [Point(center.x - 1, center.y),
            Point(center.x, center.y),
            Point(center.x + 1, center.y),
            Point(center.x + 1, center.y + 1)]
        Shape.__init__(self, coords, "orange")

class L_shape(Shape):
    def __init__(self, center):
        coords = [Point(center.x - 1, center.y + 1),
            Point(center.x - 1, center.y),
            Point(center.x, center.y),
            Point(center.x + 1, center.y)]
        Shape.__init__(self, coords, "light blue")

class O_shape(Shape):
    def __init__(self, center):
        coords = [Point(center.x - 1, center.y),
            Point(center.x - 1, center.y + 1),
            Point(center.x, center.y),
            Point(center.x, center.y + 1)]
        Shape.__init__(self, coords, "red")

class S_shape(Shape):
    def __init__(self, center):
        coords = [Point(center.x + 1, center.y),
            Point(center.x, center.y),
            Point(center.x, center.y + 1),
            Point(center.x - 1, center.y + 1)]
        Shape.__init__(self, coords, "green")

class T_shape(Shape):
    def __init__(self, center):
        coords = [Point(center.x, center.y + 1),
            Point(center.x - 1, center.y),
            Point(center.x, center.y),
            Point(center.x + 1, center.y)]
        Shape.__init__(self, coords, "yellow")

class Z_shape(Shape):
    def __init__(self, center):
        coords = [Point(center.x, center.y + 1),
            Point(center.x - 1, center.y),
            Point(center.x, center.y),
            Point(center.x + 1, center.y + 1)]
        Shape.__init__(self, coords, "pink")

# To print all

win = GraphWin("Tetrominoes", 900, 150)
tetrominoes = [I_shape, J_shape, L_shape, O_shape, S_shape, T_shape, Z_shape]
x = 3
for tetromino in tetrominoes:
    shape = tetromino(Point(x, 1))
    shape.draw(win)
    x += 4

    
# FINAL NOTES
# To see Teteris game, see 'Tetrominoes.py' file 
