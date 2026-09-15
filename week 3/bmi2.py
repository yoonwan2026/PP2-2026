# 문제

# 여려 학생들의 학생들의 키와 몸무게를 리스트로 입력 받아 BMI 리스트를 출력하는 
# 함수 테스트하는 함수를 작성하시오
# BMI 함수는 지난 시간에 작성한 get_bmi 함수를 이용하여 작성하시오

students = 5
list = []
for i in range(students):
    height = float(input(f"{i+1}번째 학생의 키를 입력하세요(cm): "))
    weight = float(input(f"{i+1}번째 학생의 몸무게를 입력하세요(kg): "))
    list.append((height, weight))

def get_bmi(weight_kg: float, height_cm: float) -> float:
    bmi = weight_kg / (height_cm/100) ** 2
    return bmi

def test_get_bmi():
    for i, (height, weight) in enumerate(list, start=1):
        bmi = get_bmi(weight, height)
        print(f"{i}번째 학생: 키({height}cm), 몸무게({weight}kg) => BMI: {bmi:.2f}")

if __name__ == "__main__":
    test_get_bmi()