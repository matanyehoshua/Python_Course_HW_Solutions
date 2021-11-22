# HW Q5
# if word is less than 4 letters: break out of the loop

# inputted list
_list = ['coding of world', 'pen', 'python', 'hello']

# prints words that are longer than 4 letters, if it encounters a word smaller than 4 letters,
# it breaks out of the loop
for i in range(len(_list) // 2):
    if len(_list[i]) < 4:
        break
    else:
        print(_list[i].upper())