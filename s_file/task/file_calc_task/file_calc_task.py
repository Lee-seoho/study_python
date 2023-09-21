# 두 정수의 연산을 수행하는 계산기 모듈 제작
# 연산 수행 시 해당 시간을 기록하고,
# 연산 수행 중 오류 발생 시 오류 사항과 시간을 기록하도록 한다.

# 입력 예
# 두 정수를 입력하세요.
# 연산자를 선택하세요

# 출력 예
# 1 + 3 = 4
# 10 / 0 = ZeroDivisionError

import calculator as c
import datetime
now = datetime.datetime.now()

menu_message = "1. 계산기 사용\n2. 나가기\n"
num_message = "두 정수를 입력하세요.\n예 1 3\n"
operator_message = "연산자를 선택하세요"
choice_operator_message = "1. +\n2. -\n3. *\n4. /\n5. 나가기\n"


# 화면
#----------------------------------------------------------
while True :
    choice_menu = int(input(menu_message))
    if choice_menu == 1:

        num1, num2 = input(num_message).split(" ")

        try :

            while True:
                operator_choice = int(input(operator_message + "\n" + choice_operator_message))

                if operator_choice == 1:
                    c.add(int(num1), int(num2))


                elif operator_choice == 2:
                    c.sub(int(num1),int(num2))

                elif operator_choice == 3:
                    c.mul(int(num1),int(num2))

                elif operator_choice == 4:
                    c.divide(int(num1),int(num2))

                else:
                    break

        except ValueError:
            print(f'{num1} , {num2} = ValueError : {now}')
            print("정수를 입력하세요")

    else:
        break






