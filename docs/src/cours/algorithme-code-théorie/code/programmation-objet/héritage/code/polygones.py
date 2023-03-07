from math import sqrt


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other):
        x1 = self.x
        x2 = other.x

        y1 = self.y
        y2 = other.y

        return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


class Polygone:
    def __init__(self, points):
        self._points = tuple(points)

    def périmètre(self):
        d = 0
        pivot = self._points[0]
        for point in self._points[1:]:
            d += pivot.distance(point)
            pivot = point
        d += pivot.distance(self._points[0])

        return d

    def aire(self):
        a = 0
        pivot = self._points[0]
        for point in self._points[1:]:
            a += pivot.x * point.y - pivot.y * point.x
            pivot = point

        point = self._points[0]
        a += pivot.x * point.y - pivot.y * point.x

        return 0.5 * abs(a)


class Triangle(Polygone):
    def __init__(self, point1, point2, point3):
        super().__init__([point1, point2, point3])


points = [Point(0, 0), Point(0, 2), Point(1, 2), Point(1, 0)]
polygone = Polygone(points)
print(polygone.périmètre())
print(polygone.aire())

triangle = Triangle(Point(0, 0), Point(0, 2), Point(1, 2))
print(isinstance(triangle, Triangle))
print(isinstance(triangle, Polygone))
