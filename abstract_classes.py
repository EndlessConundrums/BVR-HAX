from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def get_perimeter(self):
        pass

    @abstractmethod
    def get_area(self):
        pass

    def print_all_info(self):
        self.get_perimeter()
        self.get_area()

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def get_perimeter(self):
        self.perimeter = (self.width * 2) + (self.height * 2)
        print(self.perimeter)
    
    def get_area(self):
        self.area = self.width * self.height
        print(self.area)

class Square(Rectangle):
    def __init__(self, width):
        self.width = width
        self.height = width

class Triangle(Shape):
    def __init__(self, sideLength):
        self.sideLength = sideLength
    
    def get_perimeter(self):
        self.perimeter = self.sideLength * 3
        print(self.perimeter)

    def get_area(self):
        self.area = (self.sideLength ** 2) / 2
        print(self.area)

aSquare = Square(5)
rectRect = Rectangle(4, 6)
triHard = Triangle(3)
aSquare.print_all_info()
rectRect.print_all_info()
triHard.print_all_info()