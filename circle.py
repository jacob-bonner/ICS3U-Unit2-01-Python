#!/usr/bin/env python3

# Created by: Jacob Bonner
# Created on: September 2019
# This program will calculate the area and perimeter of a circle

import math


def main():
    print("If the circle has a radius of 15cm:")
    print("")
    print("Area is: {}cm^2".format(math.pi*15**2))
    print("Perimeter is: {}cm".format(2*math.pi*15))


if __name__ == "__main__":
    main()
