# Page 25_9

# enters a number and stores its counter in a seperate value
x = int(input("enter a number "))
count = 1
top_number = x
for i in range(99):
    x = int(input("enter a number "))
    count += 1
    if x > top_number:
        top_number = x
        top_number_count = count

# prints the counter of the top number after the loop is done
print(f'the top number count is: {top_number_count}')