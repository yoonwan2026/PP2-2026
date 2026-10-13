# =====================================================
# 작성자 : 윤완
# 작성일 : 2026-10-13
# 문제   : 02. Address, Person을 동시에 상속받는 Contact 클래스 만들기
# 설계   : 1) Address는 street(거리), city(도시)를 저장한다.
#          2) Person은 name(이름), email(이메일)을 저장한다.
#          3) Contact는 Address와 Person을 둘 다 상속받는다(다중 상속).
#          4) Contact의 __init__()에서 부모 두 개의 __init__()을
#             각각 직접 불러서 모든 값을 저장한다.
# =====================================================


class Address:
    def __init__(self, street, city):
        self.street = str(street)
        self.city = str(city)


class Person:
    def __init__(self, name, email):
        self.name = str(name)
        self.email = str(email)


class Contact(Address, Person):
    def __init__(self, name, email, street, city):
        Address.__init__(self, street, city)
        Person.__init__(self, name, email)


my_contact = Contact("홍길동", "hong@test.com", "세종대로 1길", "서울")
print("이름 :", my_contact.name)
print("이메일 :", my_contact.email)
print("주소 :", my_contact.city, my_contact.street)