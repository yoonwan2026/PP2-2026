"""
작성자: 윤완
작성일: 2026-10-03
문제: 7번 - 사람들의 연락처를 저장하는 PhoneBook 클래스를 작성해보자.
      딕셔너리를 이용하여 연락처를 저장한다.

해결하기 위한 설계
1. 클래스
   - PhoneBook 클래스를 만든다.
2. 인스턴스 변수
   - contacts : 연락처를 저장하는 딕셔너리
     key = 이름(name)
     value = [mobile, office, email] 리스트
3. 자료구조
   - 딕셔너리(dict) 안에 리스트(list)
"""


class PhoneBook:
    def __init__(self):
        self.contacts = {}

    def add(self, name, mobile=None, office=None, email=None):
        self.contacts[name] = [mobile, office, email]

    def __str__(self):
        s = ""
        for name in self.contacts:
            x = self.contacts[name]
            s = s + name + "\n"
            if x[0] != None:
                s = s + "mobile phone: " + x[0] + "\n"
            if x[1] != None:
                s = s + "office phone: " + x[1] + "\n"
            if x[2] != None:
                s = s + "email address: " + x[2] + "\n"
            s = s + "\n"
        return s.rstrip("\n")


def test_prob7():
    obj = PhoneBook()
    obj.add("Kim", office="1234567", email="kim@company.com")
    obj.add("Park", office="2345678", email="park@company.com")
    print(obj)


if __name__ == "__main__":
    test_prob7()