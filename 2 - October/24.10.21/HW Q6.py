# HW Q6

my_name = 'Matan Yehoshua'
a_count = 0
b_count = 0
a = 0
b = 0
counter = 0

# print the last 5 letters of the string
print(my_name[-5:])
# prints the first third of the string
print(my_name[0:len(my_name) // 3])
# counts the amount of times the letter 'a' in written in the string
for i in range(len(my_name)):
    if my_name[i] == 'a':
        a_count += 1
print(a_count)
# checks if the letter 'b' is present in  the string, if so prints "True" if not, prints "False"
for i in range(len(my_name)):
    if my_name[i] == 'b':
        b_count = True
        break
    else:
        b_count = False
print(b_count)
# prints the string words separately
print(my_name.split())
# Prints the last name first, then prints the first name
print(my_name[6:], my_name[0:5])
# Upper-cases the last name
print(my_name[6:].upper())
# replaces the first name's middle letter to *
print(my_name[0:5].replace("t", "*"))
# Prints the full name with the first name's middle letter replaced to *
print(my_name.replace("t", "*"))


