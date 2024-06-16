import numpy as np
import matplotlib.pyplot as plt

from functools import cmp_to_key, reduce
import random
from typing import List

from utils.intersection import Point

# https://web.archive.org/web/20120115045246/http://tixxit.net/2010/03/graham-scan
def _keep_left(hull, r):
    while len(hull) > 1 and turn(hull[-2], hull[-1], r) != TURN_LEFT:
            hull.pop()
    if not len(hull) or hull[-1] != r:
        hull.append(r)
    return hull


def graham_scan(points):
    points = sorted(points)
    l = reduce(_keep_left, points, [])
    u = reduce(_keep_left, reversed(points), [])
    return l.extend(u[i] for i in range(1, len(u) - 1)) or l


def calculate_partial_hulls(m, points: Point = []):
    partitions = [points[i:i+m] for i in range(0, len(points), m)]
    hulls = []
    
    for partition in partitions:
        hull = []
        if len(partition) > 3:
            hull = graham_scan(partition)
        else:
            hull = partition
        hulls.append(hull)

    return hulls

# https://gist.github.com/tixxit/242402
TURN_LEFT, TURN_RIGHT, TURN_NONE = (1, -1, 0)

# Zwraca kierunek
# -1 dla prawego
# 0 dla prosto
# 1 dla lewego
def turn(p, q, r):
    return np.sign((q.x - p.x)*(r.y - p.y) - (r.x - p.x)*(q.y - p.y))

# Zwraca natępny punkt otoczki w kierunku zgodnym ze wskazówkami zegara od p
def _next_hull_pt(points, p):
    q = p
    for r in points:
        t = turn(p, q, r)
        if t == TURN_RIGHT or t == TURN_NONE and p.Distance(r) > p.Distance(q):
            q = r
    return q


# jarvis march
def _convex_hull(points):
    hull = [min(points)]
    for p in hull:
        q = _next_hull_pt(points, p)
        if q != hull[0]:
            hull.append(q)
    return hull


def calculate_hull(points: Point = []):
    final_hull = False
    partial_hulls = []

    if len(points) > 3:
        partial_hulls = calculate_partial_hulls(6, points)
        unique_points = set()
        for hull in partial_hulls:
            for point in hull:
                unique_points.add(point)
        final_hull = _convex_hull(list(unique_points))
    else:
        partial_hulls = points
        final_hull = points
    
    return {
        'convex_hull': final_hull,
		'partial_hulls': partial_hulls
    }


"""Rysuje otoczke wypukla
pierwszy argument - wszystkie punkty na plaszczyznie
drugi argument - punkty otoczki wypuklej"""
def draw_convex_hull(points: Point = [], convex_hull_points: Point = []):
    points_as_tuples = [(point.x, point.y) for point in points]
    convex_hull_points_as_tuples = [(point.x, point.y) for point in convex_hull_points]

    plt.scatter(*zip(*points_as_tuples), color='blue')
    plt.scatter(*zip(*convex_hull_points_as_tuples), color='red')

    for line_index in range(len(convex_hull_points_as_tuples) - 1):
        x_coords = [convex_hull_points_as_tuples[line_index][0], convex_hull_points_as_tuples[line_index + 1][0]]
        y_coords = [convex_hull_points_as_tuples[line_index][1], convex_hull_points_as_tuples[line_index + 1][1]]

        plt.plot(x_coords, y_coords, color="blue")

    plt.plot([convex_hull_points_as_tuples[0][0], convex_hull_points_as_tuples[len(convex_hull_points_as_tuples) - 1][0]],
            [convex_hull_points_as_tuples[0][1], convex_hull_points_as_tuples[len(convex_hull_points_as_tuples) - 1][1]], color="blue")

    plt.show()


def get_distance_between_all_points(points: Point = []) -> float:
    total_distance = 0.0
    for i in range(len(points) - 1):
        total_distance += points[i].Distance(points[i + 1])

    return total_distance


def generate_random_points(num_points: int, range_min: int, range_max: int) -> List[Point]:
    return [Point(random.uniform(range_min, range_max), random.uniform(range_min, range_max)) for _ in range(num_points)]


def get_points_from_text() -> List[Point]:
    points_number = int(input("Podaj ilosc punktow\n"))
    points = []

    for i in range(points_number):
        data = input()
        point = data.split(" ")
        points.append(Point(int(point[0]), int(point[1])))

    return points


if __name__ == "__main__":
    points = [Point(4, 4), Point(4, 6), Point(4, 7),
            Point(10, 10), Point(1, 1), Point(1, 1), Point(5, 6), Point(5, 7)]
    
    points1 = [Point(0, 0), Point(6, 8), Point(1, 7), Point(7, 3), Point(0, 5),
            Point(5, 5), Point(2, 8), Point(11, 2), Point(6, 9), Point(2, 1),
            Point(4, 7), Point(9, 3), Point(5, 5), Point(6, 1), Point(2, 1)]
    
    points2 = [Point(0, 0), Point(1, 1), Point(1, 4), Point(1, 12), Point(2, 4),
            Point(3, 5), Point(2, 5), Point(6, 7), Point(2, 8), Point(7, 7),
            Point(1, 9), Point(4, 5), Point(1, 8), Point(9, 2), Point(9, 10),
            Point(4, 8), Point(6, 10), Point(10, 1), Point(6, 7), Point(9, 3)]
    
    points3 = [
        Point(10, 33),
        Point(25, 47),
        Point(4, 12),
        Point(39, 22),
        Point(45, 18),
        Point(27, 30),
        Point(17, 8),
        Point(30, 42),
        Point(6, 15),
        Point(23, 9),
        Point(12, 34),
        Point(5, 28),
        Point(16, 21),
        Point(40, 49),
        Point(18, 24),
        Point(35, 36),
        Point(2, 44),
        Point(28, 3),
        Point(14, 31),
        Point(8, 26),
        Point(41, 11),
        Point(50, 39),
        Point(22, 17),
        Point(33, 13),
        Point(1, 46),
        Point(38, 19),
        Point(9, 20),
        Point(31, 6),
        Point(11, 43),
        Point(48, 7),
        Point(19, 14),
        Point(47, 29),
        Point(21, 25),
        Point(32, 37),
        Point(44, 2),
        Point(7, 40),
        Point(20, 5),
        Point(46, 1),
        Point(37, 32),
        Point(13, 35),
        Point(26, 27),
        Point(36, 4),
        Point(43, 16),
        Point(34, 23),
        Point(3, 38)
    ]

    points4 = [
        Point(42, 67),
        Point(15, 89),
        Point(73, 35),
        Point(84, 56),
        Point(23, 78),
        Point(67, 12),
        Point(45, 98),
        Point(12, 54),
        Point(90, 32),
        Point(37, 76),
        Point(54, 23),
        Point(61, 87),
        Point(30, 40),
        Point(21, 92),
        Point(79, 61),
        Point(56, 15),
        Point(34, 85),
        Point(63, 47),
        Point(92, 70),
        Point(28, 19),
        Point(77, 44),
        Point(49, 83),
        Point(88, 51),
        Point(31, 72),
        Point(66, 38),
        Point(40, 95),
        Point(13, 59),
        Point(82, 21),
        Point(58, 75),
        Point(26, 46),
        Point(72, 34),
        Point(50, 91),
        Point(35, 27),
        Point(97, 68),
        Point(19, 84),
        Point(64, 31),
        Point(85, 49),
        Point(47, 93),
        Point(25, 62),
        Point(78, 29),
        Point(51, 77),
        Point(16, 88),
        Point(83, 37),
        Point(59, 99),
        Point(36, 58)
]

    # convex_hull_points = calculate_hull(points4)['convex_hull']
    # print(convex_hull_points)
    # draw_convex_hull(points4, convex_hull_points)

    # print(get_distance_between_all_points(convex_hull_points))

    # random_points = generate_random_points(300, 0, 50)
    # convex_hull_points_2 = calculate_hull(random_points)['convex_hull']
    # draw_convex_hull(random_points, convex_hull_points_2)

    test = [
        Point(1, 10),
        Point(10, 1),
        Point(10, 10),
        Point(3, 2),
        Point(1, 1),
    ]

    test3 = [
        Point(0, 0),
        Point(1, 1),
        Point(2, 2),
        Point(3, 3),
        Point(4, 4),
        Point(5, 5),
        Point(6, 6),
        Point(7, 7),
        Point(8,8),
        Point(9, 9),
        Point(10, 10),
        Point(11, 11),
        Point(12, 12),
        Point(13, 13),
        Point(14, 14),
        Point(15, 15),
        Point(16, 16),
        Point(17, 17),
        Point(18, 18),
        Point(19, 19),
        Point(20, 20),
    ]

    test3232 = [
        Point(1.000, 0.000),
        Point(0.966, 0.259),
        Point(0.866, 0.500),
        Point(0.707, 0.707),
        Point(0.500, 0.866),
        Point(0.259, 0.966),
        Point(0.003, 1.000),
        Point(-0.259, 0.966),
        Point(-0.500, 0.866),
        Point(-0.707, 0.707),
        Point(-0.866, 0.500),
        Point(-0.966, 0.259),
        Point(-1.000, 0.000),
        Point(-0.966, -0.259),
        Point(-0.866, -0.500),
        Point(0.500, 0.200),
        Point(0.700, -0.300),
        Point(-0.300, 0.800),
        Point(0.400, 0.400),
        Point(0.200, 0.100),
        Point(-0.500, 0.100),
        Point(-0.400, -0.500),
        Point(-0.200, 0.700),
        Point(0.100, -0.200),
        Point(0.300, -0.100),
        Point(-0.100, 0.600),
        Point(0.600, -0.400),
        Point(-0.600, -0.200),
        Point(-0.700, -0.100),
        Point(0.100, 0.500),
        Point(-0.100, 0.300),
        Point(0.500, -0.600),
        Point(0.400, 0.000),
        Point(-0.300, -0.400),
        Point(-0.200, -0.600),
        Point(-0.500, -0.300),
        Point(0.600, 0.300),
        Point(0.700, 0.400),
        Point(-0.600, 0.600),
        Point(-0.700, 0.700),
        Point(0.200, -0.700),
        Point(0.300, 0.200),
        Point(-0.100, -0.500),
        Point(0.100, -0.300),
        Point(0.700, -0.600),
        Point(0.600, -0.700),
        Point(-0.200, -0.100),
        Point(-0.300, 0.100),
        Point(0.400, 0.500),
        Point(-0.400, 0.200),
        Point(0.500, -0.400),
        Point(-0.600, -0.500),
        Point(-0.700, 0.500),
        Point(0.200, -0.300),
        Point(0.300, 0.400)
    ]

    hull = calculate_hull(points1)['convex_hull']
    draw_convex_hull(points1, hull)

    print(hull)


    # print(test_hull)

    # print(points3)
    # draw_convex_hull(points3, convex_hull_points_2)

    # sub = calculate_hull(points3)['partial_hulls']

    # for s in sub:
    #     print(f"{len(s)}", s)

    # p = get_points_from_text()
    # print(p)