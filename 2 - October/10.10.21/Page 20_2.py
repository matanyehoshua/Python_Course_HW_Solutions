# Page 20_2

# inputs a grade number
x = int(input("enter a grade: "))

# checks what number is the grade and gives it a verbal result
if x < 55:
    print("not enough")
elif x >= 55 and x <= 64:
    print('enough')
elif x >= 65 and x <= 74:
    print('almost good')
elif x >= 75 and x <= 84:
    print('good')
elif x >= 85 and x <= 94:
    print('very good')
elif x >= 95:
    print('great')