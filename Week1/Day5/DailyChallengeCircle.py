
import math
import turtle

class Circle:
    def __init__(self, radius=None, diameter=None):
        if radius is not None:
            self.radius = radius
        elif diameter is not None:
            self.radius = diameter / 2
        else:
            raise ValueError("Either radius or diameter must be provided.")
    
    @property
    def diameter(self):
        return self.radius * 2
    
    @diameter.setter
    def diameter(self, value):
        self.radius = value / 2
    
    @property
    def area(self):
        return math.pi * (self.radius ** 2)
    
    def __str__(self):
        return f"Circle(radius={self.radius}, diameter={self.diameter}, area={self.area:.2f})"
    
    def __repr__(self):
        return f"Circle({self.radius})"
    
    def __add__(self, other):
        if isinstance(other, Circle):
            return Circle(self.radius + other.radius)
        return NotImplemented
    
    def __lt__(self, other):
        if isinstance(other, Circle):
            return self.radius < other.radius
        return NotImplemented
    
    def __le__(self, other):
        if isinstance(other, Circle):
            return self.radius <= other.radius
        return NotImplemented
    
    def __eq__(self, other):
        if isinstance(other, Circle):
            return self.radius == other.radius
        return NotImplemented
    
    def __ne__(self, other):
        if isinstance(other, Circle):
            return self.radius != other.radius
        return NotImplemented
    
    def __gt__(self, other):
        if isinstance(other, Circle):
            return self.radius > other.radius
        return NotImplemented
    
    def __ge__(self, other):
        if isinstance(other, Circle):
            return self.radius >= other.radius
        return NotImplemented

def draw_circles(circles):
    turtle.speed(0)
    turtle.penup()
    x_position = -200
    
    for circle in circles:
        turtle.goto(x_position, -circle.radius)
        turtle.pendown()
        turtle.circle(circle.radius)
        turtle.penup()
        x_position += circle.diameter + 10
    
    turtle.done()

# Example usage:
c1 = Circle(radius=5)
c2 = Circle(diameter=10)
c3 = Circle(radius=7)

print(c1)  # Circle(radius=5, diameter=10, area=78.54)
print(c2)  # Circle(radius=5, diameter=10, area=78.54)
print(c3)  # Circle(radius=7, diameter=14, area=153.94)

c4 = c1 + c3  # New circle with radius 12
print(c4)  # Circle(radius=12, diameter=24, area=452.39)

print(c1 < c3)  # True
print(c1 == c2)  # True

circles = [c3, c1, c4, c2]
circles_sorted = sorted(circles)
print(circles_sorted)

draw_circles(circles_sorted)
