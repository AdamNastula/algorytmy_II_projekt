import math
import matplotlib.pyplot as plt
import dataclasses
import numpy as np


@dataclasses.dataclass(frozen=True)
class Point:
    x: int
    y: int

    def Distance(self, point):
        return math.sqrt(math.pow((point.x - self.x), 2) + math.pow((point.y - self.y), 2))


def det(a: Point, b: Point, c: Point) -> int:
    n_array = np.array([[a.x, a.y, 1], [b.x, b.y, 1], [c.x, c.y, 1]])
    return int(np.linalg.det(n_array))


"""sprawdza, czy punkt znajduje sie na prostej"""
def is_on_line(a: Point, b: Point, c: Point) -> bool:
    if c.x < a.x == c.x < b.x:
        return False
    if c.y < a.y == c.y < b.y:
        return False
    if (b.x - a.x)*(c.y - a.y) != (c.x - a.x)*(b.y - a.y):
        return False
    return True


"""sprawdza wspolliniowosc"""
def check_multicollinearity(a: Point, b: Point, c: Point, d: Point) -> bool:
    # a miedzy c i d
    if min(c.x, d.x) <= a.x <= max(c.x, d.x) and min(c.y, d.y) <= a.y <= max(c.y, d.y):
        return True
    # b miedzy c i d
    elif min(c.x, d.x) <= b.x <= max(c.x, d.x) and min(c.y, d.y) <= b.y <= max(c.y, d.y):
        return True
    # c miedzy a i b
    elif min(a.x, b.x) <= c.x <= max(a.x, b.x) and min(a.y, b.y) <= c.y <= max(a.y, b.y):
        return True
    # d miedzy a i b
    elif min(a.x, b.x) <= d.x <= max(a.x, b.x) and min(a.y, b.y) <= d.y <= max(a.y, b.y):
        return True
    return False


"""sprawdza, czy proste sie przecinaja"""
def intersection(a: Point, b: Point, c: Point, d: Point) -> bool:
    first_det = det(a, b, c)
    second_det = det(a, b, d)

    if first_det > 0 > second_det or first_det < 0 < second_det:
        return True
    elif (is_on_line(a, b, c) or is_on_line(a, b, d)) and check_multicollinearity(a, b, c, d):
        return True
    return False

"""wyswietla graficzna reprezentacje odcinkow"""
def draw_graphic(axis, a: Point, b: Point, c: Point, d: Point):
    axis.plot([a.x, b.x], [a.y, b.y], color="blue")
    axis.plot([c.x, d.x], [c.y, d.y], color="blue")
    axis.set_title(f"A: ({a.x}, {a.y}), B: ({b.x}, {b.y}), C: ({c.x}, {c.y}), D: ({d.x}, {d.y})")

if __name__ == "__main__":
    print(intersection(
        Point(2, 2),
        Point(10, 7),
        Point(3, 8),
        Point(8, 1)
    ))  # tak

    print(intersection(
        Point(1, 2),
        Point(7, 6),
        Point(7, 3),
        Point(9, 1)
    ))  # nie
    
    print(intersection(
        Point(1, 1),
        Point(5, 5),
        Point(3, 3),
        Point(6, 6)
    ))  # tak

    print(intersection(
        Point(1, 1),
        Point(5, 5),
        Point(3, 3),
        Point(4, 4)
    ))  # tak

    print(intersection(
        Point(1, 1),
        Point(5, 5),
        Point(3, 3),
        Point(5, 2)
    ))  # tak

    print(intersection(
        Point(1, 1),
        Point(5, 5),
        Point(6, 6),
        Point(7, 7)
    ))  # nie

    print(intersection(
        Point(2, 2),
        Point(4, 4),
        Point(5, 4),
        Point(8, 4)
    ))  # nie

    print(intersection(
        Point(2, 1),
        Point(4, 3),
        Point(4, 3),
        Point(4, 6)
    ))  # tak

    print(intersection(
        Point(2, 1),
        Point(2, 6),
        Point(2, 5),
        Point(5, 5)
    ))  # tak

    print(intersection(
        Point(1, 3),
        Point(3, 3),
        Point(5, 3),
        Point(7, 3)
    ))  # nie

    """axis - wymiar tablicy, na ktorej beda rysowane grafy, w tym przypadku 2x2"""
    figure, axis = plt.subplots(2, 2, figsize=(12, 12)) 

    """axis w tej funkcji wyznacza pozycje, na ktorej bedzie narysowany graf"""
    drawGraphic(
        axis[0, 0],
        Point(1, 3),
        Point(3, 3),
        Point(5, 3),
        Point(7, 3))
    
    drawGraphic(
        axis[0, 1],
        Point(2, 1),
        Point(2, 6),
        Point(2, 5),
        Point(5, 5))
    
    drawGraphic(
        axis[1, 0],
        Point(2, 1),
        Point(4, 3),
        Point(4, 3),
        Point(4, 6)
    )

    drawGraphic(
        axis[1, 1],
        Point(2, 2),
        Point(4, 4),
        Point(5, 4),
        Point(8, 4)
    )

    plt.show()
