"""
작성자: 윤완
작성일: 2026-10-03
문제: 2번 - 로켓을 나타내는 Rocket 클래스를 작성해보자.

해결하기 위한 설계
1. 클래스
   - Rocket 클래스를 만든다.
2. 인스턴스 변수
   - x, y : 현재 로켓의 위치 (기본값은 0, 0)
3. 자료구조
   - 위치는 정수(int) 두 개로 저장한다.
"""


class Rocket:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"

    def moveUp(self):
        self.y = self.y + 1


def test_prob2():
    myRocket = Rocket()
    print("로켓의 높이:", myRocket.y)

    myRocket.moveUp()
    print("로켓의 높이:", myRocket.y)


if __name__ == "__main__":
    test_prob2()