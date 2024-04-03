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


class Segment:

    def __init__(self, points):
        self.segment = ((points[0].get_x(), points[0].get_y()), (points[1].get_x(), points[1].get_y()))
        self.one_intersection = ''
        print(self.segment)

    def intersections(self):
        if (self.segment[0][0] > 0 and self.segment[0][1] > 0) and (self.segment[1][0] < 0 and self.segment[1][1] > 0):
            Segment.one_intersection = True
        elif (self.segment[0][0] < 0 and self.segment[0][1] > 0) and (self.segment[1][0] < 0 and self.segment[1][1] < 0):
            Segment.one_intersection = True
        elif (self.segment[0][0] < 0 and self.segment[0][1] < 0) and (self.segment[1][0] > 0 and self.segment[1][1] > 0):
            Segment.one_intersection = True
        elif (self.segment[0][0] > 0 and self.segment[0][1] < 0) and (self.segment[1][0] > 0 and self.segment[1][1] > 0):
            Segment.one_intersection = True
        else:
            Segment.one_intersection = False
        return Segment.one_intersection


class CoordinateSystem:
    segments = []

    @staticmethod
    def add_segment(segment):
        segment_addition = Segment(segment)
        CoordinateSystem.segments.append(segment_addition)

    @staticmethod
    def axis_intersection():
        counter = 0
        for elem in CoordinateSystem.segments:
            if elem.intersections() is True:
                counter += 1
        return counter


system1 = CoordinateSystem()
system1.add_segment((Point((3, 4)), Point((-5, 4))))
system1.add_segment((Point((-1, 4)), Point((-5, 4))))
system1.add_segment((Point((-3, 4)), Point((5, -4))))
print(system1.axis_intersection())
