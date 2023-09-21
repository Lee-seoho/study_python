from crud import save, find_all, update, delete, find_by_id
import random as r
from send_messages import send_many
import re
from email_send import send_email
import json


# 사용자가 입력한 문장을 영어로 번역
# 한국어와 번역된 문장을 DBMS에 저장
# 번역 내역 조회

# 업로드한 이미지 파일의 이름과 이미지의 내용을 DBMS에 저장(OCR API)



# 아이디 중복검사
# 회원가입(SMS API) - 랜덤한 인증번호 6자리 발송 후 검사
# 회원 비밀번호 변경(EMAIL API) - 랜덤한 인증번호 10자리 발송 후 검사
#랜덤한 6자리 숫자
# def random_number():
#     result = ''
#     for i in range(6):
#         result += str(r.randint(0, 9))
#     return result
#
# def message_out(input_phone_number,random_number):
#     data = {
#         'messages': [
#             {
#                 'to': f'{input_phone_number}',
#                 'from': '01046577163',
#                 'text': f'인증번호 : {random_number}.'
#             }
#         ]
#     }
#     res = send_many(data)
#     # print(json.dumps(res.json(), indent=2, ensure_ascii=False))
#
#
#
# menu = "1.회원가입\n2.비밀번호변경\n3.나가기\n"
# error_message = '잘못 입력 했습니다.'
# input_email_message = '이메일을 입력하세요\n'
# input_password_message = '패스워드를 입력하세요\n'
# input_phone_number_message = '휴대폰번호를 입력하세요 예)01012341234\n'
# email_check = re.compile('^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
#
# find_all_query = 'select id, account_email, account_password, account_number from tbl_account'
# tbl_account = find_all(find_all_query)
#
# while True:
#     choice = int(input(menu))
#     if choice == 1:
#         while True:
#             id_choice = input(input_email_message)
#             if email_check.match(id_choice) != None:
#                 for row in tbl_account:
#                     if row['account_email'] == id_choice:
#                         print('중복된 이메일 입니다.')
#                         break
#                     else:
#                         input_password = input(input_password_message)
#                         input_phone_number = input(input_phone_number_message)
#                         random_number = random_number()
#                         message_out(input_phone_number, random_number)
#                         input_certification_number = input('인증번호를 입력하세요\n')
#                         if input_certification_number == random_number:
#                             insert_query = 'INSERT INTO tbl_account(account_email, account_password, account_number) ' \
#                                            'VALUES(%s ,%s, %s)'
#                             insert_params =[id_choice, input_password, input_phone_number]
#                             save(insert_query,insert_params)
#                             print('인증완료! 회원가입에 성공했습니다')
#                         else:
#                             print('인증번호를 잘 못 입력 하셨습니다.')
#                             break
#             else:
#                 print('이메일 형식이 아닙니다! 다시 입력하세요')
#                 break
#
#     elif choice == 2:
#         input_email = input('이메일을 입력하세요')
#         for i in range(len(tbl_account)):
#             if tbl_account[i]['account_email'] == input_email:
#                 check_password = input('기존비밀번호 입력해주세요')
#                 if tbl_account[i]['account_password'] == check_password:
#                     print('입력에 성공했습니다! 이메일로 인증번호가 올때까지 기다리세요!')
#                     identify_email = send_email()
#                     new_password, identify_number = map(str, input('새로운 비밀번호와 메일 인증번호를 입력하세요 예)1234 12345ABcde\n').split(' '))
#                     if identify_email == identify_number:
#                         update_query = "UPDATE tbl_account SET account_password= %s WHERE account_email = %s "
#                         update_param = [new_password, input_email]
#                         update(update_query, update_param)
#                         print('비밀번호가 변경 되었습니다.')
#                         break
#                     else:
#                         print('인증번호가 일치하지 않습니다.')
#                         break
#                 else:
#                     print('비밀번호를 잘못 입력하셨습니다.')
#                     break
#             else:
#                 print('존재하지 않는 이메일입니다.')
#                 break
#
#     elif choice == 3:
#         break
#     else:
#         print(error_message)



from papago import papapgo_translation
# 사용자가 입력한 문장을 영어로 번역
# 한국어와 번역된 문장을 DBMS에 저장
# 번역 내역 조회

# input_korean = input('번역하고 싶은 한글을 입력하세요\n')
# translate_english = papapgo_translation(input_korean)
# print(f'{input_korean} 번역하면 {translate_english} 입니다.')
#
# insert_query = "INSERT INTO tbl_translate (translate_korean, translate_eng) VALUES( %s, %s)"
# insert_param = [input_korean, translate_english]
# save(insert_query, insert_param)

# find_all_query = 'select id, translate_korean, translate_eng from tbl_translate'
# print(find_all(find_all_query))


# 업로드한 이미지 파일의 이름과 이미지의 내용을 DBMS에 저장(OCR API)
# from ocr import ocr_image
#
# image = input('글자가 있는 이미지의 주소를 입력하세요')
# content = ocr_image(image)
# # print(content)
#
# insert_quary = 'INSERT INTO tbl_ocr (ocr_title, ocr_content) VALUES(%s, %s)'
# insert_param = [image, content]
# save(insert_quary, insert_param)