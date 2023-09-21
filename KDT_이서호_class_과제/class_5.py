# 로그인
# 아이디, 비밀번호 모두 일치하면 "환영합니다" 출력
# 아이디 혹은 비밀번호가 일치하지 않으면 해당 내용이 "일치하지 않습니다" 출력

class LogIn:
    def __init__(self, information):
        self.information = information


    def login(self):
        if user.id in self.information.keys():
            if self.information.get(user.id) == user.password:
                print("환영합니다.")
            else :
                print('비밀번호가 일치하지 않습니다.')
        else :
            print('아이디가 일치하지 않습니다.')

class User:
    def __init__(self, id, password):
        self.id = id
        self.password = password


login = LogIn({
    'red12' : 'apple123',
    'blue34' : 'banana456',
    'green56' : 'tomato789'
})

user = User('red12', 'apple123')

login.login()