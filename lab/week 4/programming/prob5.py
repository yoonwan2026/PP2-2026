"""
작성자: 윤완
작성일: 2026-10-03
문제: 5번 - 삼각형을 나타내는 Triangle 클래스를 작성해보자.

해결하기 위한 설계
1. 클래스
   - Triangle 클래스를 만든다.
2. 인스턴스 변수
   - a, b, c : 삼각형의 세 각도 (angle1, angle2, angle3)
   - n       : 변의 개수 (numberOfSides), 기본값 3
3. 테스트
   - test_prob5()에서 Triangle(90, 30, 60)의 checkAngles()를 확인한다.
"""


class Triangle:
    def __init__(self, a1, a2, a3):
        self.a = a1
        self.b = a2
        self.c = a3
        self.n = 3

    def __str__(self):
        return "각도: " + str(self.a) + ", " + str(self.b) + ", " + str(self.c) + " / 변의 개수: " + str(self.n)

    def getAngle1(self):
        return self.a

    def getAngle2(self):
        return self.b

    def getAngle3(self):
        return self.c

    def setAngle1(self, x):
        self.a = x

    def setAngle2(self, x):
        self.b = x

    def setAngle3(self, x):
        self.c = x

    def checkAngles(self):
        return self.a + self.b + self.c == 180


def test_prob5():
    triangle = Triangle(90, 30, 60)
    print(triangle.checkAngles())


if __name__ == "__main__":
    test_prob5()