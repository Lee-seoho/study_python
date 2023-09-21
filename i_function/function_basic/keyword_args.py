# keyword arguments
# def introduce(**info):
#     print(type(info))
#     print(info)
#     print(f'name: {info.get("name")}')
#     print(f'email: {info.get("email")}')

def introduce(name, email):
    print(f'name: {name}')
    print(f'email: {email}')

# dict를 그대로 보내면 TypeError 발생!
# introduce({"name": '한동석', "email": 'tedhan1204@gmail.com'})

print("*" * 10)
# 직접 key=value를 작성하는 방법
introduce(name='한동석', email='tedhan1204@gmail.com')

print("*" * 10)

# packing을 발생시키는 방법
introduce(**{"name": '한동석', "email": 'tedhan1204@gmail.com'})
print("*" * 10)

# dict를 담은 후 packing 발생!
info = {"name": '한동석', "email": 'tedhan1204@gmail.com'}
introduce(**info)
print("*" * 10)

# unpacking
info = {"name": '한동석', "email": 'tedhan1204@gmail.com'}
print("*" * 10)

# key만 추출되어 전달
introduce(*info)
print("*" * 10)

# value를 추출하기 위해서는 **info로 사용해야 한다.
introduce(**info)
print("*" * 10)


introduce(name='한동석', email='tedhan1204@gmail.com')

introduce(name='한동석', email='tedhan1204@gmail.com')