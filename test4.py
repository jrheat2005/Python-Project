

# Parent Class
class Shape:
    def area(self):
        pass

# Child Class
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2

# Child Class   
class Rectangle(Shape):
    def __init__(self,width,height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# Create instances
circle = Circle(5)
rectangle = Rectangle(4, 6)

# Calculate
shapes = [circle, rectangle]
for shape in shapes:
    print(f"Area: {shape.area()}")





    
