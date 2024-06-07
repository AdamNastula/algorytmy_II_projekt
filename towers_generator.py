import random


def generate_towers(number_of_towers, number_of_flatlanders, rest_frequency, range_min, range_max):
    print(number_of_towers)

    for i in range(number_of_towers):
        print(f"{random.randint(range_min, range_max)} {random.randint(range_min, range_max)} {random.randint(1, 100)}")

    print(rest_frequency)


if __name__ == "__main__":
    generate_towers(25, 3, 5, 1, 100)