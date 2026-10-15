# ============================================================
# 작성자 : 윤완
# 작성일 : 2026-10-14
# 문제   : 이터레이터를 구현하는 MyEnumerate 클래스를 작성한다. (인덱스, 요소) 튜플을 반환한다.
# 설계   :
#   1. __init__에서 자료 구조(a)와 인덱스(i = 0)를 저장한다.
#   2. __iter__는 자기 자신(self)을 반환한다.
#   3. __next__에서 i가 길이 이상이면 StopIteration을 일으켜 반복을 끝낸다.
#   4. 아니면 (i, a[i]) 튜플을 만들고 i를 1 증가시킨 뒤 반환한다.
# ============================================================

class MyEnumerate:
    def __init__(self, a):
        self.a = a
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i >= len(self.a):
            raise StopIteration
        b = (self.i, self.a[self.i])
        self.i += 1
        return b


for i, c in MyEnumerate('abc'):
    print(f"{i} : {c}")