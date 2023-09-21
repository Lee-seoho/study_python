from crud import save, find_all, update, delete, find_by_id
import hashlib

# insert_query = "insert into tbl_member(member_id, member_password, member_name)" \
#                "values(%s, %s, %s)"
# 암호화
# encrypt = hashlib.sha256()
# encrypt.update('5555'.encode('utf-8'))
# print(encrypt.hexdigest())
# insert_param = ['lss5555', encrypt.hexdigest(), '이순신']
# delete_query = "delete from tbl_member where member_name = %s"
# delete_param = ['이순신']
# find_all_query = "select id, member_id, member_password, member_name from tbl_member"
# update_query = "update tbl_member set member_name = %s where member_id = %s"
# update_param = ['한동숙', 'lss5555']
# find_by_id_query = "select id, member_id, member_password, member_name from tbl_member " \
#                    "where id = %s"
# find_by_id_param = ['8']
# 회원가입
# save(insert_query, insert_param)
# 전체 조회
# for i in find_all(find_all_query):
#     print(f'아이디: {i.get("member_id")}\n이름: {i.get("member_name")}')
# 아이디가 'hds1234'인 회원의 이름을 '한동숙'으로 수정
# update(update_query, update_param)
# 이름이 '이순신'인 회원 삭제
# delete(delete_query, delete_param)
# 회원 번호로 한 명 조회
# print(find_by_id(find_by_id_query, find_by_id_param))

# 단일 테이블 3개 제작 후 CRUD 진행

# 1. 상품 정보 추가
# insert_query = "insert into tbl_product(product_name, product_price, created_date) " \
#                "values(%s, %s, %s)"
# insert_param = ['마우스', 45000, '2023-07-03']
# save(insert_query, insert_param)

# 상품 정보 조회
# find_by_id_query = "select product_name, product_price, created_date from tbl_product " \
#              "where id = %s"
# find_by_id_param = [1]
# product = find_by_id(find_by_id_query, find_by_id_param)
# print(str(product.get('created_date')))

# 2. 학생 정보 추가
insert_query = "insert into tbl_student(student_name, student_birth) " \
               "values(%s, %s)"
insert_param = ['김혜빈', '2000-03-23T01:41:35']

save(insert_query, insert_param)

# ------------------------------------------------------------------------------------------

