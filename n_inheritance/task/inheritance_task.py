# 상속 실습

# 정사각형 (Square)
#   └─ 정육면체 (Cube)

#  1. '정사각형' 객체 정의
#  클래스 이름 : Square
#  생성자 : '한 면의 길이(side)'를 받아서 초기화
#  면적을 계산하여 리턴하는 메소드 : getArea()

# 2. '정육면체' 객체 정의 <-- Square 상속받아 정의
#  클래스 이름 : Cube
#  getArea() : 정육면체의 총 면적(겉넓이, 각 면적의 합)
#  getVolume() : 정육면체의 부피 계산

# 타입 데코레이터
# 동적바인딩인 파이썬에서 선언 시 타입을 알려줄 수 있는 문법
# 변수명: 자료형, 변수명 뒤에 자료형을 작성한다.
# def function() -> 리턴타입:, 함수의 선언부에서 소괄호 뒤에 자료형을 작성한다.
class Square:
    def __init__(self, side):
        self.side = side

    def get_area(self):
        area = self.side ** 2
        return  area

class Cube(Square):
    # def __init__(self, side):
    #     super().__init__(side)

    def get_area(self):
        area = super().get_area() * 6
        return area

    def get_volume(self):
        volume = self.side ** 3
        return volume


a = Square(3)
print(a.get_area())

b = Cube(2)
print(b.get_area(), b.get_volume())