from functools import cmp_to_key
import random
import intersection as intersection
import math
import numpy as np
import matplotlib.pyplot as plt
from typing import List

def calculate_distance(a: intersection.Point, b: intersection.Point) -> int:
    return (a.x - b.x)**2 - (a.y - b.y)**2
    
def get_area_between_3_points(a: intersection.Point, b: intersection.Point, c: intersection.Point) -> float:
    return ((b.x - a.x) * (a.y - c.y) - (c.x - a.x) * (a.y - b.y))
    
def get_angle_between_3_points(a: intersection.Point, b: intersection.Point, c: intersection.Point) -> float:
    ab = math.sqrt(math.pow(b.x - a.x, 2) + math.pow(b.y - a.y, 2))
    bc = math.sqrt(math.pow(b.x - c.x, 2) + math.pow(b.y - c.y, 2))
    ac = math.sqrt(math.pow(c.x - a.x, 2) + math.pow(c.y - a.y, 2))

    arccos = (pow(bc, 2) + pow(ab, 2) - pow(ac, 2)) / (2 * bc * ab)

    if (abs(arccos) - 1) < 0.00001: 
        arccos = np.clip(arccos, -1, 1)

    return math.acos(arccos)

def check_left_turn(a: intersection.Point, b: intersection.Point, c: intersection.Point) -> bool:
    return get_area_between_3_points(a, b, c) > 0

"""liczy kat miedzy punktami, wartosc jest podana w radianach"""
def angle_to_point(lowest_point: intersection.Point, compared_point: intersection.Point) -> float:
    return math.atan2(lowest_point.y - compared_point.y, compared_point.x - lowest_point.x)

"""zwraca polozony najnizej na plaszczyznie punkt"""
def find_lowest_point(points: intersection.Point = []) -> intersection.Point:
    lowest_point = points[0]

    for point in points:
        if point.y > lowest_point.y:
            lowest_point = point
        elif point.y == lowest_point.y and point.x < lowest_point.x:
            lowest_point = point

    return lowest_point

def is_same_point(a: intersection.Point, b: intersection.Point) -> bool:
    if not a or not b:
        return False
    return a.x == b.x and a.y == b.y

def sort_points_by_angle(lowest_point: intersection.Point, points: intersection.Point = []):
    points.sort(key=cmp_to_key(lambda a, b: (
        -1 if a.y == lowest_point.y and a.x == lowest_point.x else
        1 if b.y == lowest_point.y and b.x == lowest_point.x else
        1 if angle_to_point(lowest_point, a) > angle_to_point(lowest_point, b) else -1
    )))

    return points

def graham_scan(points: intersection.Point = []):
    lowest_point = find_lowest_point(points)

    if (lowest_point):
        sort_points_by_angle(lowest_point,points)
    
    """zwracamy od razu punkty, jesli jest ich 4 lub mniej, bo wtedy graham scan nie jest potrzebny"""
    if len(points) < 4:
        return points
    
    unique_points = set(points)
    points = list(unique_points)

    sort_points_by_angle(lowest_point, points)
    
    stack: intersection.Point = []
    stack.append(points[0])
    stack.append(points[1])

    index: int = 2
    stack_length: int = 2

    while index < len(points):
        stack_length = len(stack)

        if stack_length > 1:
            left = check_left_turn(stack[stack_length - 2], stack[stack_length - 1], points[index])
            
            if (left):
                stack.append(points[index])
                index += 1
            else:
                stack.pop()
        else:
            stack.append(points[index])
            index += 1

    return stack

def tangentBinarySearch(hull, a, b):
    def find_angle(parameter: int):
        if is_same_point(b, hull[parameter]):
            return -999
        else:
            return get_angle_between_3_points(a, b, hull[parameter])

    length = len(hull)

    start = 0
    end = length - 1
    left_split = -1
    right_split = -1
    search_size = (end - start) + 1

    if search_size == 1:
        return 0
    elif search_size == 2:
        angle0 = find_angle(0)
        angle1 = find_angle(1)

        if angle0 > angle1:
            return 0
        return 1
    
    while search_size > 2:
        search_size = (end - start) + 1

        start_angle = find_angle(start)
        end_angle = find_angle(end)

        split = math.floor(search_size / 2) + start
        mid = None
        if search_size % 2 == 0:
            left_split = split - 1
            right_split = split
        else:
            mid = split
            left_split = split - 1
            right_split = split + 1
        

        left_angle = find_angle(left_split)
        right_angle = find_angle(right_split)
        
        if mid is not None:
            mid_angle = find_angle(mid)
        else:
            mid_angle = -9999

        max_left = max(start_angle, left_angle)
        max_right = max(right_angle, end_angle)

        if mid_angle >= left_angle and mid_angle >= right_angle:
            return mid
        
        elif max_left > max_right:
            end = left_split
            if start_angle == left_angle:
                return end
        else:
            start = right_split
            if right_angle == end_angle:
                return start
            
    return start

def jarvis_march(m, sub_hulls):
    if len(sub_hulls) == 1:
        return sub_hulls[0]

    sub_hulls.sort(key=cmp_to_key(lambda a, b: (
        1 if a[0].y < b[0].y else -1
    )))

    convex_hull = []
    convex_hull.append(sub_hulls[0][0])
    point0 = intersection.Point(0, convex_hull[0].y)

    for i in range(int(m)):
        max_angle = -99999999
        pk1 = None
        last = point0 if i == 0 else convex_hull[i - 1]

        for j in range(len(sub_hulls)):
            result = tangentBinarySearch(sub_hulls[j], last, convex_hull[i])
            angle = get_angle_between_3_points(last, convex_hull[i], sub_hulls[j][result])

            if not math.isnan(angle) and angle > max_angle:
                max_angle = angle
                pk1 = sub_hulls[j][result]

        if pk1.x == convex_hull[0].x and pk1.y == convex_hull[0].y:
            return convex_hull
        
        convex_hull.append(pk1)

    return False
    

def calculate_partial_hulls(m, points: intersection.Point = []):
    partition = []
    partition.append([])
    ph_index = 0

    for i in range(len(points)):
        if i >= (ph_index + 1) * m:
            ph_index += 1
            partition.append([])
        partition[ph_index].append(points[i])

    hulls = []
    
    for i in range(len(partition)):
        hull = graham_scan(partition[i])
        hulls.append(hull)

    return hulls

def calculate_hull(points: intersection.Point = []):
    final_hull = False
    partial_hulls = []

    if len(points) > 3:
        exp = 1
        while final_hull == False:
            m = math.pow(2, math.pow(2, exp))
            partial_hulls = calculate_partial_hulls(m, points)
            final_hull = jarvis_march(m, partial_hulls)
            exp += 1
    else:
        final_hull = points
    
    return {
        'convex_hull': final_hull,
		'partial_hulls': partial_hulls
    }

"""Rysuje otoczke wypukla
pierwszy argument - wszystkie punkty na plaszczyznie
drugi argument - punkty otoczki wypuklej"""
def draw_convex_hull(points, convex_hull_points):
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


def generate_random_points(num_points: int, range_min: int, range_max: int) -> List[intersection.Point]:
    return [intersection.Point(random.randint(range_min, range_max), random.randint(range_min, range_max)) for _ in range(num_points)]


if __name__ == "__main__":
    points = [intersection.Point(4, 4), intersection.Point(4, 6), intersection.Point(4, 7),
            intersection.Point(10, 10), intersection.Point(1, 1), intersection.Point(1, 1), intersection.Point(5, 6), intersection.Point(5, 7)]
    
    points1 = [intersection.Point(0, 0), intersection.Point(6, 8), intersection.Point(1, 7), intersection.Point(7, 3), intersection.Point(0, 5),
            intersection.Point(5, 5), intersection.Point(2, 8), intersection.Point(11, 2), intersection.Point(6, 9), intersection.Point(2, 1),
            intersection.Point(4, 7), intersection.Point(9, 3), intersection.Point(5, 5), intersection.Point(6, 1), intersection.Point(2, 1)]
    
    points2 = [intersection.Point(0, 0), intersection.Point(1, 1), intersection.Point(1, 4), intersection.Point(1, 12), intersection.Point(2, 4),
            intersection.Point(3, 5), intersection.Point(2, 5), intersection.Point(6, 7), intersection.Point(2, 8), intersection.Point(7, 7),
            intersection.Point(1, 9), intersection.Point(4, 5), intersection.Point(1, 8), intersection.Point(9, 2), intersection.Point(9, 10),
            intersection.Point(4, 8), intersection.Point(6, 10), intersection.Point(10, 1), intersection.Point(6, 7), intersection.Point(9, 3)]
    
    points3 = [
        intersection.Point(10, 33),
        intersection.Point(25, 47),
        intersection.Point(4, 12),
        intersection.Point(39, 22),
        intersection.Point(45, 18),
        intersection.Point(27, 30),
        intersection.Point(17, 8),
        intersection.Point(30, 42),
        intersection.Point(6, 15),
        intersection.Point(23, 9),
        intersection.Point(12, 34),
        intersection.Point(5, 28),
        intersection.Point(16, 21),
        intersection.Point(40, 49),
        intersection.Point(18, 24),
        intersection.Point(35, 36),
        intersection.Point(2, 44),
        intersection.Point(28, 3),
        intersection.Point(14, 31),
        intersection.Point(8, 26),
        intersection.Point(41, 11),
        intersection.Point(50, 39),
        intersection.Point(22, 17),
        intersection.Point(33, 13),
        intersection.Point(1, 46),
        intersection.Point(38, 19),
        intersection.Point(9, 20),
        intersection.Point(31, 6),
        intersection.Point(11, 43),
        intersection.Point(48, 7),
        intersection.Point(19, 14),
        intersection.Point(47, 29),
        intersection.Point(21, 25),
        intersection.Point(32, 37),
        intersection.Point(44, 2),
        intersection.Point(7, 40),
        intersection.Point(20, 5),
        intersection.Point(46, 1),
        intersection.Point(37, 32),
        intersection.Point(13, 35),
        intersection.Point(26, 27),
        intersection.Point(36, 4),
        intersection.Point(43, 16),
        intersection.Point(34, 23),
        intersection.Point(3, 38)
    ]

    points4 = [
        intersection.Point(42, 67),
        intersection.Point(15, 89),
        intersection.Point(73, 35),
        intersection.Point(84, 56),
        intersection.Point(23, 78),
        intersection.Point(67, 12),
        intersection.Point(45, 98),
        intersection.Point(12, 54),
        intersection.Point(90, 32),
        intersection.Point(37, 76),
        intersection.Point(54, 23),
        intersection.Point(61, 87),
        intersection.Point(30, 40),
        intersection.Point(21, 92),
        intersection.Point(79, 61),
        intersection.Point(56, 15),
        intersection.Point(34, 85),
        intersection.Point(63, 47),
        intersection.Point(92, 70),
        intersection.Point(28, 19),
        intersection.Point(77, 44),
        intersection.Point(49, 83),
        intersection.Point(88, 51),
        intersection.Point(31, 72),
        intersection.Point(66, 38),
        intersection.Point(40, 95),
        intersection.Point(13, 59),
        intersection.Point(82, 21),
        intersection.Point(58, 75),
        intersection.Point(26, 46),
        intersection.Point(72, 34),
        intersection.Point(50, 91),
        intersection.Point(35, 27),
        intersection.Point(97, 68),
        intersection.Point(19, 84),
        intersection.Point(64, 31),
        intersection.Point(85, 49),
        intersection.Point(47, 93),
        intersection.Point(25, 62),
        intersection.Point(78, 29),
        intersection.Point(51, 77),
        intersection.Point(16, 88),
        intersection.Point(83, 37),
        intersection.Point(59, 99),
        intersection.Point(36, 58)
]

    convex_hull_points = calculate_hull(points)['convex_hull']
    print(convex_hull_points)
    draw_convex_hull(points, convex_hull_points)

    # random_points = generate_random_points(100, 0, 200)
    # convex_hull_points_2 = calculate_hull(random_points)['convex_hull']
    # print(convex_hull_points_2)
    # draw_convex_hull(random_points, convex_hull_points_2)