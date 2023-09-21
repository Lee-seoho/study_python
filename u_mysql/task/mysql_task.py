from crud import save, find_all, update, delete, find_by_id, all_id
import hashlib

message = "회원가입\n아이디 비밀번호 이름을 입력하세요\n예)hgd 1234 홍길동\n"
# menu = "1.회원가입\n2.비밀번호변경\n3.나가기\n"
# error_message = '잘못 입력 했습니다.'
# input_email = '이메일을 입력하세요\n'
# input_password_message = '패스워드를 입력하세요\n'
# input_phone_number_message = '휴대폰번호를 입력하세요 예)01012341234\n'

# find_all_query = 'select id, account_email, account_password, account_number from tbl_account'
# tbl_account = find_all(find_all_query)

# while True:
#     choice = int(input(menu))
#     if choice == 1:
#         while True:
#             id_choice = input(input_email)
#             if email_check.match(id_choice) != None:
#                 for row in tbl_account:
#                     if row['account_email'] == id_choice:
#                         print('중복된 이메일 입니다.')
#                         break
member_id, member_password, member_name = input(message).split(" ")
insert_query = "insert into tbl_member(member_id, member_password, member_name)" \
               "values(%s, %s, %s)"

encrypt = hashlib.sha256()
encrypt.update(member_password.encode('utf-8'))

insert_param = [member_id, encrypt.hexdigest(), member_name]


find_all_query = "select id, member_id, member_password, member_name from tbl_member"
find_all(find_all_query)
target_id = "select member_id from tbl_member"
all_id(target_id)

for target in all_id(target_id):
    if member_id == target.get('member_id'):
        print("중복된 아이디 입니다.")
        break

    else:
        save(insert_query, insert_param)
        print("사용가능한 아이디 입니다.")


# # for i in find_all(find_all_query):
#     print(f'아이디: {i.get("member_id")}\n이름: {i.get("member_name")}')

# 아이디 중복검사
# 회원가입(SMS API) - 랜덤한 인증번호 6자리 발송 후 검사
# 회원 비밀번호 변경(EMAIL API) - 랜덤한 인증번호 10자리 발송 후 검사

# 사용자가 입력한 문장을 영어로 번역
# 한국어와 번역된 문장을 DBMS에 저장
# 번역 내역 조회

# 업로드한 이미지 파일의 이름과 이미지의 내용을 DBMS에 저장(OCR API)