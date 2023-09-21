# python -m pip install PyMySQL
# python -m pip install cryptography

import pymysql
conn = pymysql.connect(host='127.0.0.1', user='root', password='1234', db='app', charset='utf8')
cursor = conn.cursor(pymysql.cursors.DictCursor)
# cursor.execute("insert into tbl_member(member_id, member_password, member_name) values('hds1234', '1234', '한동석')")
# conn.commit()

cursor.execute("select id, member_id, member_password, member_name from tbl_member")
rows = cursor.fetchall()
print(rows)

cursor.close()
conn.close()