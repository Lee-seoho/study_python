class A:
    pass


class B:
    pass


class C:
    pass


# 클래스를 담아놓고
classes = [A, B, C]

# 사용시 ()를 붙이면, __new__(), __init__()이 순서대로 호출된다.
a = classes[0]()