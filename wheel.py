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

    win = GraphWin("My Circle", 100, 100)
    c = Circle(Point(50,50), 10)
    c.draw(win)
    win.getMouse() 
    win.close()

# grey circle
# sample()




def square1():

    win = GraphWin("My Square", 500, 500)
    square = Rectangle(Point(100,100), Point(400,400))
    square.setFill("Red")
    square.draw(win)
    win.getMouse() 
    win.close()

# Red square
# square1()



class Wheel():

    def __init__(self, center, wheel_radius, tire_radius):
        self.tire_circle = Circle(center, tire_radius)
        self.wheel_circle = Circle(center, wheel_radius)

    def draw(self, win): 
        self.tire_circle.draw(win) 
        self.wheel_circle.draw(win) 

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

    def move(self, dx, dy): 
        self.tire_circle.move(dx, dy) 
        self.wheel_circle.move(dx, dy)

    def animate(self, win, dx, dy, n):
        if n > 0:
            self.move(dx, dy)
            win.after(100, self.animate, win, dx, dy, n-1)

def wheel_yellow():
    new_win = GraphWin('Wheel', 700, 500) 

    wheel_center = Point(200, 200) # The wheel center is a Point at (200, 200)
    tire_radius = 100  # The radius of the outer tire is 100
    new_wheel = Wheel(wheel_center, 0.6*tire_radius, tire_radius)

    new_wheel.set_color('yellow', 'orange')
    new_wheel.draw(new_win)
    
    new_wheel.animate(new_win, 10, 0, 100)
    new_win.mainloop()

def wheel_orange():
    new_win = GraphWin('Wheel', 700, 500) 

    wheel_center = Point(200, 200) # The wheel center is a Point at (200, 200)
    tire_radius = 100  # The radius of the outer tire is 100
    new_wheel = Wheel(wheel_center, 0.6*tire_radius, tire_radius)

    new_wheel.set_color('orange', 'red')
    new_wheel.draw(new_win)
    
    new_wheel.animate(new_win, 10, 0, 100)
    new_win.mainloop()

# wheel2 = wheel_orange()
# whee1l = wheel_yellow()
