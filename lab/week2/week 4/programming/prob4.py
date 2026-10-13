"""
작성자: 윤완
작성일: 2026-10-03
문제: 4번 - 사각형을 나타내는 Rectangle 클래스를 작성해보자.

해결하기 위한 설계
1. 클래스
   - Rectangle 클래스를 만든다.
2. 인스턴스 변수
   - x, y : 사각형의 좌측 상단 좌표
   - w, h : 사각형의 너비(width)와 높이(height)
"""


class Rectangle:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ", " + str(self.w) + ", " + str(self.h) + ")"

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getWidth(self):
        return self.w

    def getHeight(self):
        return self.h

    def setX(self, a):
        self.x = a

    def setY(self, a):
        self.y = a

    def setWidth(self, a):
        self.w = a

    def setHeight(self, a):
        self.h = a

    def getArea(self):
        return self.w * self.h

    def overlap(self, r):
        if self.x < r.x + r.w and r.x < self.x + self.w:
            if self.y < r.y + r.h and r.y < self.y + self.h:
                return True
        return False


def test_prob4():
    r1 = Rectangle(0, 0, 100, 100)
    r2 = Rectangle(10, 10, 100, 100)
    if r1.overlap(r2):
        print("r1과 r2는 서로 겹칩니다.")
    else:
        print("r1과 r2는 서로 겹치지 않습니다.")


if __name__ == "__main__":
    test_prob4()