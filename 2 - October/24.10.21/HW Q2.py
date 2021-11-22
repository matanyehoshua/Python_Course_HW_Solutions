# HW Question N2:

#takes a question from the user
_question = input("Please enter your question: ")
list_question = _question.split()
print(list_question)
num1 = float(list_question[0])
sign = list_question[1]
num2 = float(list_question[2])
second_sign = list_question[3] # not necessary
answer = float(list_question[4])


# checks what the sign of the question and answers according to the sign:

if sign == '+':
    print (answer == num1 + num2)
elif sign == '-':
    print (answer == num1 - num2)
elif sign == '*':
    print(answer == num1 * num2)
elif sign == "/":
    print(answer == num1 / num2)
else:
    print('unknown sign')