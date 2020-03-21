#!/usr/bin/python3
#LaneDoyle
#3/20/2020

'''Program to calculate the area of a trapezoid'''

print("Area of a trapezoid")

height = float(input("Enter the height of the trapezoid: "))
length_bottom = float(input("Enter the length of the bottom base: "))
length_top = float(input("Enter the length of the top base: "))

area = 1/2 * (length_bottom + length_top) * height

print("The area is: ", area)    