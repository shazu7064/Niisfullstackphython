from abc import ABC, abstractmethod

# Abstract class
class Shape(ABC):

    @abstractmethod
    def perimeter(self):
        pass


# Child class
class Rectangle(Shape):

    def __init__(self, l, b):
        self.length = l
        self.breadth = b

    def perimeter(self):
        return 2 * (self.length + self.breadth)


# Another child class
class Square(Shape):

    def __init__(self, s):
        self.side = s

    def perimeter(self):
        return 4 * self.side


# Object creation
r = Rectangle(10, 5)
s = Square(4)

print("Rectangle Perimeter =", r.perimeter())
print("Square Perimeter =", s.perimeter())