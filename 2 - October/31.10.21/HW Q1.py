# HW Q1

# fruits = [“apple”, “banana”, “cherry”, “kiwi”, “mango”].
# create a list of all the fruits with the letter ‘a’ inside them using list comprehension
a_fruits = []
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

# creates a list of 'a' lettered fruits and adds the fruits with 'a' letter in them
for word in fruits:
    if 'a' in word:
        a_fruits.append(word)
print(a_fruits)