import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Line:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def __str__(self):
        return '(' + str(self.point1.x) + ', ' + str(self.point1.y) + \
            ' to ' + str(self.point2.x) + ', ' + str(self.point2.y) + ')'

    def length(self):
        dx = self.point2.x - self.point1.x
        dy = self.point2.y - self.point1.y
        return math.sqrt(dx ** 2 + dy ** 2)

    def midpoint(self):
        x_mid = (self.point1.x + self.point2.x) / 2
        y_mid = (self.point1.y + self.point2.y) / 2
        return Point(x_mid, y_mid)

    def x_projection(self):
        return abs(self.point2.x - self.point1.x)

    def y_projection(self):
        return abs(self.point2.y - self.point1.y)


if __name__ == '__main__':
    dot1 = Point(1, 2)
    dot2 = Point(4, 6)

    line = Line(dot1, dot2)

    print(line)
    print(line.length())
    mid = line.midpoint()
    print(f'Midpoint: {mid.x}, {mid.y}')
    print(line.x_projection())
    print(line.y_projection())
