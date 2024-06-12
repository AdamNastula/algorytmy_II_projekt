# to korzysta z modulow, nie mozna tego wlaczac w normalny sposob, trzeba w konsoli, w glownym folderze wlaczyc
# python -m problem1.solve_1b

from problem1.solve_1a import test
from utils import intersection
import utils.chans_algorithm as ch

if __name__ == "__main__":
    points = [
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
    # test wlacza solve_1a.py
    test()
    print("Punkty orientacyjne krainy maja nastepujace koordynaty x i y:")
    print(points)
    print("\nPunkty wykorzystane do zbudowania plotu maja nastepujace koordynaty:")

    fence = ch.calculate_hull(points)['convex_hull']
    print(fence)
    ch.draw_convex_hull(points, fence)