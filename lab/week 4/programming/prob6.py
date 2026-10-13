"""
작성자: 윤완
작성일: 2026-10-03
문제: 6번 - Person 클래스를 작성해보자.

해결하기 위한 설계
1. 클래스
   - Person 클래스를 만든다.
"""


class Person:
    def __init__(self, name, mobile="없음", office="없음", email="없음"):
        self.n = name
        self.m = mobile
        self.o = office
        self.e = email

    def __str__(self):
        s = self.n + "\n"
        s = s + "mobile phone: " + self.m + "\n"
        s = s + "office phone: " + self.o + "\n"
        s = s + "email address: " + self.e
        return s

    def getName(self):
        return self.n

    def getMobile(self):
        return self.m

    def getOffice(self):
        return self.o

    def getEmail(self):
        return self.e

    def setName(self, a):
        self.n = a

    def setMobile(self, a):
        self.m = a

    def setOffice(self, a):
        self.o = a

    def setEmail(self, a):
        self.e = a


def test_prob6():
    p1 = Person("Kim", office="1234567", email="kim@company.com")
    p2 = Person("Park", office="2345678")
    p2.setEmail("park@company.com")
    print('p1 = Person("Kim", office="1234567", email="kim@company.com")')
    print('p2 = Person("Park", office="2345678")')
    print('p2.setEmail("park@company.com")')


if __name__ == "__main__":
    test_prob6()