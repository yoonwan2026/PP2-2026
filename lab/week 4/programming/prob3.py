"""
작성자: 윤완
작성일: 2026-10-03
문제: 3번 - 상자를 나타내는 Box 클래스를 작성하여  보자 Box 클래스는 상자의 가로, 세로, 높이를 나타내는 인스턴스 변수를 가진다.

해결하기 위한 설계
1. 클래스
   - Box 클래스를 만든다.
2. 인스턴스 변수
   - x : 상자의 가로(length)
   - y : 상자의 세로(height)
   - z : 상자의 높이(depth)
3. 자료구조
   - 숫자(int) 3개
"""


class Box:
    def __init__(self, l, h, d):
        self.x = l
        self.y = h
        self.z = d

    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ", " + str(self.z) + ")"

    def getLength(self):
        return self.x

    def getHeight(self):
        return self.y

    def getDepth(self):
        return self.z

    def setLength(self, a):
        self.x = a

    def setHeight(self, a):
        self.y = a

    def setDepth(self, a):
        self.z = a


def test_prob3():
    b1 = Box(100, 100, 100)
    print(b1)
    print("상자의 부피는", b1.getHeight() * b1.getLength() * b1.getDepth())


if __name__ == "__main__":
    test_prob3()