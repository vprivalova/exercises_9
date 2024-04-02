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
        space = ((self.dot[1]-self.dot[0])**2 - (other[1] - other[0])**2)**0.5
        return space

    def sum(self, other):
        new_x = self.dot[0] + other[0]
        new_y = self.dot[1] + other[1]
        new_point = Point((new_x, new_y))
        return new_point


point1 = Point((3, 5))
print(point1.get_x())
print(point1.get_y())
print(point1.distance((4, 3)))
print(str(point1))
print(point1.sum((6, 7)))
