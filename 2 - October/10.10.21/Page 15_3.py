#Page 15_3

diameter = int(input("enter a diameter"))
depth = int(input("enter the depth"))
pi = 3.14
r = 0.5 * diameter

# calculates the total capacity:
capacity = pi * (r ** 2) * depth

print("the total capacity of the cooking pot is: ", capacity)