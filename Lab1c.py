#!/usr/bin/python3
#LaneDoyle
#3/20/2020

import math as mt

'''Program to calculate the area of a circle'''

print("Area of a circle:")

radius = float(input("Please enter the radius of the circle: "))

area = mt.pi * (radius ** 2)

print("The area of the circle is ", area, " sq. cm")