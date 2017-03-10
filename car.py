# Valerie Lim
# Date: 10 March 2017
# Homework 8 - Graphics and Classes
# Title: Car.py

# Exercise 4.2

from graphics import *
from wheel import *

# sample to call from other doc
# wheel.wheel_orange()


def make_point():

    win = GraphWin("My Square", 300, 300)
    center = Point(50, 50)
    x = center.getX()
    c = Circle(Point(50, 50), x+10)
    c.draw(win)
    win.getMouse() 
    win.close()

        
class Car:
    def __init__(self, wheel1_center, wheel1_radius, wheel2_center, wheel2_radius, car_height):
        self.wheel1 = Circle(wheel1_center, wheel1_radius)
        self.wheel2 = Circle(wheel2_center, wheel2_radius)
        Point1 = wheel1_center
        newX = wheel2_center.getX()
        newY = wheel2_center.getY() - car_height
        Point2 = Point(newX, newY)
        self.body = Rectangle(Point1, Point2)

    def draw(self, win):
        self.wheel1.draw(win)
        self.wheel2.draw(win)
        self.body.draw(win)

    def set_color(self, wheel1_color, wheel2_color, body_color):
        self.wheel1.setFill(wheel1_color) 
        self.wheel2.setFill(wheel2_color)
        self.body.setFill(body_color)
        
    def move(self, dx, dy): 
        self.wheel1.move(dx, dy) 
        self.wheel2.move(dx, dy)
        self.body.move(dx, dy)
        
    def animate(self, win, dx, dy, n):
        if n > 0:
            self.move(dx, dy)
            win.after(100, self.animate, win, dx, dy, n-1)


def car1():
    new_win = GraphWin("A Car", 700, 300)
    
    car1 = Car(Point(50, 50), 15, Point(100,50), 15, 40)
    car1.draw(new_win)

    car1.set_color("black", "grey", "pink")
    
    car1.animate(new_win, 1, 0, 400)
    new_win.mainloop()

car1()

