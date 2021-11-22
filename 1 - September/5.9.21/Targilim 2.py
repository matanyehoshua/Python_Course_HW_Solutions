#2. input a number. check if the number is 0 or 1, if so print '0 or 1'
#     otherwise check if the number is -1, if so print '-1'
#     otherwise print 'unknown number'
a = int(input('Enter a number'))

if a == 0 or a == 1:
    print ('0 or 1')
else:
    if a == -1:
        print(-1)
    else:
        print('unknown number')