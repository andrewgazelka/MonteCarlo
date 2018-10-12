# Monte Carlo Method https://www.i-programmer.info/babbages-bag/274-monte-carlo-or-bust.html

import random


def calc_pi(iterations: int = 10000, circle_diameter: float = 1):
    """

    We will solve pi by first drawing a circle in the center of a square with side length d. Both are centered at the
    origin.

    | The area of the circle will be proportional to the area of the square.

    | This is kinda common sense (and I'm sure a basic geometry axiom)... if you don't want to use common sense though,
    we can see how we can get any circle-square combination by transforming each shape with a matrix, A

    | k 0
    | 0 k

    | the area scaling factor is det(A) = k^2 for both of them. Thus, the area of the circle is proportional to d^2
    (the area of the square). We will be trying to figure out the c such that {the area of the circle} * c is d^2

    | This is the ratio between the area of circle and d^2. However,
    c * {the area of the circle} = d^2 = (2r)^2 = 4r^2.

    Thus, (4/c)r^2 = {the area of the circle}

    :return: pi
    """

    area_square = circle_diameter * circle_diameter
    r = circle_diameter / 2  # radius of the circle

    r_squared = r * r

    hit = 0
    miss = 0

    for i in range(iterations):

        rand_x = random.uniform(-r, r)
        rand_y = random.uniform(-r, r)

        dist2 = mag2(rand_x, rand_y)
        if dist2 < r_squared:
            hit += 1
        else:
            miss += 1

    area_circle = hit / (hit + miss) * area_square
    area_ratio = area_square / area_circle  # = c
    return 4 / area_ratio


def mag2(x, y):
    return x * x + y * y


def normal_dist(nums):
    result = 0
    for i in range(nums):
        result += i / nums
    return result


if __name__ == "__main__":
    print(calc_pi(iterations=1_000_000, circle_diameter=2))
