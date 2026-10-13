# =====================================================
# 작성자 : 윤완
# 작성일 : 2026-10-13
# 문제   : 01. Point 클래스와 Point를 상속받은 Point3D 클래스 만들기
# 설계   : 1) Point 클래스는 x, y를 받아서 저장하고
#             __str__()에서 "(x, y)" 모양의 글자를 돌려준다.
#          2) Point3D 클래스는 Point를 상속받는다.
#             x, y는 부모(Point)에게 맡기고 z만 새로 저장한다.
#          3) Point3D의 __str__()은 "(x, y, z)" 모양으로 돌려준다.
# =====================================================


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"


class Point3D(Point):
    def __init__(self, x, y, z):
        super().__init__(x, y)  
        self.z = z

    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ", " + str(self.z) + ")"


p1 = Point(1, 2)
p2 = Point3D(3, 4, 5)
print(p1)
print(p2)