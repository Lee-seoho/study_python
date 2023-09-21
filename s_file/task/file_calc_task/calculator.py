import datetime
now = datetime.datetime.now()

file = open('calculator.txt', 'w', encoding='utf-8')
file.write("계산 결과:\n")
file.close()
def add(number1, number2):

    result = number1 + number2
    print(f'{number1} + {number2} = {result}  : {now}')


def sub(number1, number2):
    result = number1 - number2
    print(f'{number1} - {number2} = {result}  : {now}')

def mul(number1, number2):
    result = number1 * number2
    print(f'{number1} * {number2} = {result}  : {now}')

def divide(number1, number2):
    result = 0
    try:
        result = number1 / number2
        print(f'{number1} / {number2} = {result}  : {now}')

    except ZeroDivisionError:
        print(f'{number1} / {number2} = ZeroDivisionError  : {now}')
        print("0으로 나눌 수 없습니다.")





