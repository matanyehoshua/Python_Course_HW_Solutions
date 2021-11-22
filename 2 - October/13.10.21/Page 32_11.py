
#not working need to test more
n = int(input("Enter a number: "))
x = int(input("Enter a number: "))
_total = 0

if n > x:
   bigger = n
   smaller = x
else:
    bigger = x
    smaller = n
for i in range(bigger + 1):
    _total += 1
    print(_total)