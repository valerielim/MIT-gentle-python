# Valerie Lim
# Date: 10 March 2017
# Homework 8 - Graphics and Classes
# Title: Car.py

# Exercise 4.2

from graphics import *
from wheel import *

        
class Car(Wheel):
    def __init__(self, wheel1_center, wheel1_radius, wheel2_center, wheel2_radius, car_height):
        self.wheel1 = Wheel(wheel1_center, wheel1_radius*0.6, wheel1_radius)
        self.wheel2 = Wheel(wheel2_center, wheel2_radius*0.6, wheel2_radius)
        Point1 = wheel1_center
        newX = wheel2_center.getX()
        newY = wheel2_center.getY() - car_height
        Point2 = Point(newX, newY)
        self.body = Rectangle(Point1, Point2)

    def draw(self, win):
        self.wheel1.draw(win)
        self.wheel2.draw(win)
        self.body.draw(win)

    def set_color(self, wheel_color, tire_color, body_color):
        # tire is outer layer
        # wheel is inner layer
        self.body.setFill(body_color)

        # THIS IS WHERE IM STUCKKKKKK :(
        # How to add colour to wheel & tire through Wheel class?
        self.wheel1.set_color(wheel_color, tire_color)
        self.wheel2.set_color(wheel_color, tire_color)
        
    def move(self, dx, dy): 
        self.wheel1.move(dx, dy) 
        self.wheel2.move(dx, dy)
        self.body.move(dx, dy)
        
    def animate(self, win, dx, dy, n):
        if n > 0:
            self.move(dx, dy)
            win.after(100, self.animate, win, dx, dy, n-1)


# Example of a Wheel object that works fine on its own: 
def wheel_blackgrey(wheel_center, tire_radius):
    # wheel_center should be a Point(x, y) object
    # tire_radius refers to Outer tire radius
    new_wheel = Wheel(wheel_center, 0.6*tire_radius, tire_radius)
    new_wheel.set_color("grey", "black")
    new_wheel.draw(new_win)
    new_wheel.animate(new_win, 10, 0, 100)
    new_win.mainloop()


# This is the syntax given from the notes. Expected to use this
# function to create a car! 
def car1():
    car1 = Car(Point(50, 50), 15, Point(100,50), 15, 40)
    car1.draw(new_win)
    car1.set_color("grey", "black", "pink")
    
    car1.animate(new_win, 1, 0, 400)
    new_win.mainloop()


# main window for this assignment:
new_win = GraphWin("A Car", 700, 300)


# test
car1()



# --------- Other notes -----------

# Syntax to call items from other doc
# wheel.wheel_orange()

def make_point():
    win = GraphWin("My Square", 300, 300)
    center = Point(50, 50)
    x = center.getX()
    c = Circle(Point(50, 50), x+10)
    c.draw(win)
    win.getMouse() 
    win.close()
