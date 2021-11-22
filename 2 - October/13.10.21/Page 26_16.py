# Page 26_16

x = int(input("Enter a positive number"))
y = int(input("Enter another positive number"))
z = 0

# checks if x and y are positive numbers
if x or y < 0:
    print("Not a positive Number!")
if y < 0:
    print("Not a positive number!")

# sums x input y times and stores the result in z, then prints z
for i in range(y):
    z += x

print(z)

