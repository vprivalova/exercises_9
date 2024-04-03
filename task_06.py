class Point:
    def __init__(self, dot=(0, 0)):
        self.dot = dot

    def get_x(self):
        x = self.dot[0]
        return x

    def get_y(self):
        y = self.dot[1]
        return y

    def __str__(self):
        return f'x coordinate: {self.dot[0]}, y coordinate: {self.dot[1]}'

    def distance(self, other):
        space = ((self.get_x() - self.get_y())**2 - (other.get_x() - other.get_y())**2)**0.5
        return space

    def sum(self, other):
        new_x = self.get_x() + other.get_x()
        new_y = self.get_y() + other.get_y()
        new_point = Point((new_x, new_y))
        return new_point


point1 = Point((3, 5))
print(point1.get_x())
print(point1.get_y())
print(point1.distance(Point((4, 3))))
print(str(point1))
print(point1.sum(Point((6, 7))))
