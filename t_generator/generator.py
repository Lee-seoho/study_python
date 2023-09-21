
def increase(number: int = 0):
    while True:
        number += 1
        yield number


result = increase()
while True:
    data = input("다음[y/N] >> ")
    if data == 'y':
        print(next(result))
    else:
        break