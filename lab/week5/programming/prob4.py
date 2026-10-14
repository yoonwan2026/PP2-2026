import random

# =====================================================
# 작성자 : 윤완
# 작성일 : 2026-10-13
# 문제   : 04. 주사위 게임 - Dice와 FraudDice 클래스 만들기
# 설계   : 1) Dice의 roll()은 random으로 1~6 중 하나를 뽑아서 돌려준다.
#          2) FraudDice는 Dice를 상속받는다(가짜 주사위).
#          3) FraudDice의 roll()을 오버라이딩해서
#             나온 값이 3 이하이면 4 이상이 나올 때까지 다시 던진다.
# =====================================================


class Dice:
    def roll(self):
        number = random.randint(1, 6)
        return number


class FraudDice(Dice):
    def roll(self):
        number = random.randint(1, 6)
        while number <= 3:  # 3 이하이면 다시 던진다
            number = random.randint(1, 6)
        return number


dice = Dice()
fraud_dice = FraudDice()
print("정상 주사위 :", dice.roll(), dice.roll(), dice.roll())
print("가짜 주사위 :", fraud_dice.roll(), fraud_dice.roll(), fraud_dice.roll())