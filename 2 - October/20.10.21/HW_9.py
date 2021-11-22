# HW_9

# functions:
def add(x = 0, y = 0):
    _add = x + y
    return (_add)

def sub(x = 0, y = 0):
    _sub = x - y
    return (_sub)

def mul(x = 0, y = 0):
    _mul = x * y
    return (_mul)

def div(x = 0, y = 0):
    if y == 0:
        _div = 'cannot divide by 0'
        return (_div)
    else:
        _div = x / y
        return (_div)

# inputs 2 values , adds, subs, muls, divs the values and prints them:
x = float(input("enter the first number: "))
y = float(input("enter the second number: "))
_add = add(x, y)
_sub = sub(x, y)
_mul = mul(x, y)
_div = div(x, y)

print(f'the sum of x + y is: {_add}')
print(f'the sub of x - y is: {_sub}')
print(f'the mul of x * y is: {_mul}')
print(f'the div of x / y is: {_div}')
