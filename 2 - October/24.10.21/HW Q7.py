# HW Q7

_string = "Hello world!"
count = 0

# prints the locations of the 'o' letters
for i in range(len(_string)):
    if _string[i] == 'o':
        print (f'the locations of the "o" letters are: {i}')

# prints the letters until the first 'o'
for i in range(len(_string)):
    if _string[i] == 'o':
        print(_string[0:i])
        break

# prints the rest of the sentence from the second 'o' letter until the end of the sentence
for i in range(len(_string)):
    if _string[i] == 'o':
        count += 1
        if count == 2:
            print(_string[i:])
            break