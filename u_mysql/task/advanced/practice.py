from crud import *
from random import randint


# class Staff :
#
#     hour_wage = 5000
#     staff_number = 5
#
#     def __init__(self, nickname, total_pay, business_hour, bonus = 0, place='청담동'):
#         self.nickname = nickname
#         self.total_pay = total_pay
#         self.business_hour = business_hour
#         self.bonus = bonus
#         self.place = place
#
#
#
#     def pay_calculator(self):
#         self.total_pay = 0
#         self.total_pay = Staff.hour_wage * self.business_hour + self.bonus
#
#
#
# person1 = Staff("토끼", 0, 3, 1000, '청담동')
# print(person1.pay_calculator())


# 학부모 회원가입
insert_query = 'insert into tbl_parent(parent_name, parent_age, parent_address, parent_phone, parent_gender)' \
               'values(%s, %s, %s, %s, %s,)'

name = input('이름: ')
age = input('나이: ')
address = input('주소: ')
phone = input('핸드폰 번호: ')
gender = input('성별: ')

parent_datas = [name, age, address, phone, gender]

parent_id = save_with_seq(insert_query, parent_datas).get('seq')

# # 아이가 있다면 아이의 정보까지 입력
insert_query = 'insert into tbl_child(child_name, child_age, child_gender, parent_id)' \
               'values(%s, %s, %s, %s)'
while True:
    choice = input("아이의 정보를 입력 하시겠습니까? [y/N]")
    if choice == 'N':
        break

    child_name = input('아이 이름 : ')
    child_age = input('아이 나이 : ')
    child_gender = input('아이 성별 : ')
    child_datas = [child_name, child_age, child_gender, parent_id]

    save(insert_query, child_datas)




