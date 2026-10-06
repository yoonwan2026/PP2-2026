"""
작성자: 윤완
작성일: 2026-10-03
문제: 1번 - 고양이를 클래스로 정의하고 몇 개의 인스턴스를 생성해보자.
      접근자와 설정자를 사용해보자.

해결하기 위한 설계
1. 클래스
   - Cat 클래스를 만든다.
2. 인스턴스 변수
   - x : 고양이의 이름
   - y : 고양이의 나이
3. 자료구조
   - 이름은 문자열(str), 나이는 정수(int)
"""


class Cat:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return self.x + " " + str(self.y)

    def getName(self):
        return self.x

    def getAge(self):
        return self.y

    def setName(self, a):
        self.x = a

    def setAge(self, b):
        self.y = b


def test_prob1():
    missy = Cat('Missy', 3)
    lucky = Cat('Lucky', 5)
    print(missy)
    print(lucky)


if __name__ == "__main__":
    test_prob1()