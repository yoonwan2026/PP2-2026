# =====================================================
# 작성자 : 윤완
# 작성일 : 2026-10-13
# 문제   : 03. Function 클래스와 2차 방정식 Quadratic 클래스 만들기
# 설계   : 1) Function 클래스의 value(x)는 아직 내용이 없다(pass).
#          2) Quadratic은 Function을 상속받고 a, b, c를 저장한다.
#          3) value(x)를 오버라이딩해서 a*x*x + b*x + c 값을 돌려준다.
#          4) get_roots()는 근의 공식으로 두 개의 근을 계산한다.
#             판별식(b*b - 4*a*c)이 0보다 작으면 실근이 없으므로 None을 돌려준다.
# =====================================================


class Function:
    def value(self, x):
        pass  # 자식 클래스에서 만들 예정


class Quadratic(Function):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def value(self, x):
        return self.a * x * x + self.b * x + self.c

    def get_roots(self):
        panbyeolsik = self.b * self.b - 4 * self.a * self.c  # 판별식
        if panbyeolsik < 0:
            return None
        root1 = (-self.b + panbyeolsik ** 0.5) / (2 * self.a)
        root2 = (-self.b - panbyeolsik ** 0.5) / (2 * self.a)
        return root1, root2


q = Quadratic(1, -3, 2)  # x*x - 3x + 2
print("x=2일 때 값 :", q.value(2))
print("두 근 :", q.get_roots())