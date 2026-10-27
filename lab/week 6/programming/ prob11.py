# ============================================================
# 작성자 : 윤완
# 작성일 : 2026-10-15
# 문제   : 원을 나타내는 Circle 클래스에 +, >, < 연산자를 중복 정의한다.
# 설계   :
#   1. Circle 클래스는 반지름(__r)을 가진다.
#   2. __add__ : 두 원의 반지름을 더한 새 Circle을 반환한다.
#   3. __gt__ : 왼쪽 원의 반지름이 더 크면 True를 반환한다.
#   4. __lt__ : 왼쪽 원의 반지름이 더 작으면 True를 반환한다.
#   5. 반지름을 확인하기 위해 get_r() 메소드를 추가한다.
# ============================================================

class Circle:
    def __init__(self, r):
        self.__r = r

    def get_r(self):
        return self.__r

    def __add__(self, o):
        return Circle(self.__r + o.__r)

    def __gt__(self, o):
        return self.__r > o.__r

    def __lt__(self, o):
        return self.__r < o.__r


a = Circle(10)
b = Circle(20)

c = a + b
print("a + b 의 반지름 =", c.get_r())
print("a > b :", a > b)
print("a < b :", a < b)