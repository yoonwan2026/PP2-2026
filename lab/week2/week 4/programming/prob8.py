"""
작성자: 윤완
작성일: 2026-10-03
문제: 8번 - printSong이라는 클래스를 작성해보자

해결하기 위한 설계
1. 클래스
   - Song 클래스를 만든다.
2. 인스턴스 변수
   - x : 노래 가사 문자열의 리스트
3. 자료구조
   - 리스트(list) 안에 문자열(str)
"""


class Song:
    def __init__(self, x):
        self.x = x

    def sing(self):
        for line in self.x:
            print(line)


def test_prob8():
    aSong = Song(["TWINKLE, twinkle, little star,",
                  "How I wonder what you are!",
                  "Up above the world so high,",
                  "Like a diamond in the sky."])
    aSong.sing()


if __name__ == "__main__":
    test_prob8()