# HW Solution 10.11.21
import math



# defines the Circle  with its radius, hekef and area
class Circle:
    def __init__(self, radius, hekef, area):
        self.radius = radius
        self.hekef = hekef
        self.area = area


# calculates the hekef and area, and prints the radius, hekef and area
    def __str__(self):
        calc_hekef = 2 * math.pi * self.radius
        calc_area = math.pi * self.radius ** 2
        print(f'the radius is: {self.radius}')
        print(f'the hekef is: {calc_hekef}')
        print(f'the area is: {calc_area}')
