


'''Create a class hierarchy for geometric shapes with the following classes:

- Shape: the base class for all shapes
- Circle: a subclass of Shape that represents a circle
- Rectangle: a subclass of Shape that represents a rectangle
- Square: a subclass of Rectangle that represents a square

Each class should have an appropriate set of instance variables and methods.
For example, the Circle class should have a radius variable and a method to calculate its area,
and the Rectangle class should have width and height variables and a method to calculate its area.'''

class Shape():
    ''''''
    def __init__(self,height, width, num_vertex) -> None:
        self.height = height
        self.width = width
        self.num_vertex = num_vertex

class Rectangle(Shape):
    def __init__(self, height, width, num_vertex) -> None:
        super().__init__(height, width, num_vertex)


    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return (self.width*2)+(self.height*2)



i = Rectangle(10,4,4)

print(i.get_area())


