# =====================================================
# 작성자 : 윤완
# 작성일 : 2026-10-13
# 문제   : 05. Animal을 상속받은 Cat 클래스와 get_oldest_cat() 함수
# 설계   : 1) Animal 클래스는 name, age를 저장한다.
#          2) Cat은 Animal을 상속받고 breed(품종)를 추가로 저장한다.
#          3) 이름과 나이가 다른 고양이 3마리를 만든다.
#          4) get_oldest_cat(*args)는 받은 고양이들을 리스트처럼 다루고
#             max()로 나이(age)가 가장 많은 고양이를 찾아서 돌려준다.
# =====================================================


class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Cat(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed


def get_oldest_cat(*args):
    oldest = max(args, key=lambda cat: cat.age)  
    return oldest


cat1 = Cat("나비", 3, "코리안숏헤어")
cat2 = Cat("치즈", 7, "러시안블루")
cat3 = Cat("까미", 5, "페르시안")

oldest_cat = get_oldest_cat(cat1, cat2, cat3)
print("가장 나이가 많은 고양이는 " + str(oldest_cat.age) + "살입니다.")