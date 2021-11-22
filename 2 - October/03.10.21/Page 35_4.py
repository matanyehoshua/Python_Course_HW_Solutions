# Ex. N4
codes = 1
_sum_approve = 0
_sum_against = 0
_sum_avoid = 0
veto = 0

# Adding up votes
while codes <= 169:
    x = int(input("Enter a Number: "))
    if x == 1:
        _sum_approve = _sum_approve + 1
    elif x == 2:
        _sum_against = _sum_against + 1
    elif x == 3:
        _sum_avoid = _sum_avoid + 1
    elif x == 4:
        break
    else:
        print ("Enter a different Number: ")
    codes = codes + 1

# Printing the Votes sums, or the Vetoing country
if x == 4:
    print ("The Country with Veto is: ", codes)
else:
    print("The sum of votes approve is: ", _sum_approve)
    print("The sum of votes against is: ", _sum_against)
    print("The sum of votes avoid is: ", _sum_avoid)

