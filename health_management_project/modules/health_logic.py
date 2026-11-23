
# AI 사용 주석
# AI 종류: ChatGPT
# AI 사용 목적: 객체지향 프로그래밍을 활용한 건강정보 관리 기능 구현 및 모듈 간 연동 방법을 이해하고, 프로그램의 완성도를 높이기 위해 활용함.
# 사용한 사람: 본인
# 사용 날짜: 2026-11-23


from modules.health_db import HealthRecord
from datetime import datetime


class HealthManager:
    """
    건강정보를 관리하는 클래스
    건강정보 추가, 조회, 수정, 삭제, 통계 기능을 담당한다.
    """

    def __init__(self, records=None):
        # 건강정보 목록을 저장한다.
        if records is None:
            self.records = []
        else:
            self.records = records

    # BMI 계산
    def calculate_bmi(self, height, weight):
        """
        키와 몸무게를 이용하여 BMI를 계산한다.
        키는 cm 단위로 입력받는다.
        """

        height = height / 100

        bmi = weight / (height * height)

        return round(bmi, 2)

    # 비만도 판정
    def calculate_status(self, bmi):
        """
        BMI 수치에 따라 비만도를 판정한다.
        """

        if bmi < 18.5:
            return "저체중"

        elif bmi < 23:
            return "정상"

        elif bmi < 25:
            return "과체중"

        else:
            return "비만"

    # 식별번호 생성
    def generate_id(self):
        """
        새로운 건강정보의 식별번호를 생성한다.
        """

        year = datetime.now().year

        number = len(self.records) + 1

        new_id = "P" + str(year) + "-" + str(number).zfill(4)

        # 기존 번호와 겹치면 번호를 증가시킨다.
        while self.search_by_id(new_id) is not None:
            number = number + 1
            new_id = "P" + str(year) + "-" + str(number).zfill(4)

        return new_id

    # 건강정보 추가
    def add_record(self, name, birth_year, gender, height, weight):
        """
        새로운 건강정보를 추가한다.
        """

        # 입력값 확인
        if height <= 0 or weight <= 0:
            return False

        # 이름과 생년이 같은 사람이 있는지 확인
        for record in self.records:
            if record.name == name and record.birth_year == birth_year:
                print("이미 등록된 사람입니다.")
                return False

        # BMI 계산
        bmi = self.calculate_bmi(height, weight)

        # 비만도 계산
        status = self.calculate_status(bmi)

        # 식별번호 생성
        patient_id = self.generate_id()

        # 건강정보 객체 생성
        new_record = HealthRecord(
            patient_id,
            name,
            birth_year,
            gender,
            height,
            weight,
            bmi,
            status
        )

        # 목록에 추가
        self.records.append(new_record)

        return True

    # 전체 목록 조회
    def get_all_records(self):
        """
        등록된 건강정보 전체 목록을 반환한다.
        """

        return self.records

    # 식별번호로 검색
    def search_by_id(self, patient_id):
        """
        식별번호를 이용하여 건강정보를 검색한다.
        """

        for record in self.records:
            if record.id == patient_id:
                return record

        return None

    # 이름으로 검색
    def search_by_name(self, name):
        """
        이름을 이용하여 건강정보를 검색한다.
        """

        result = []

        for record in self.records:
            if record.name == name:
                result.append(record)

        return result

    # 건강정보 수정
    def update_record(self, patient_id, height, weight):
        """
        기존 건강정보의 키와 몸무게를 수정한다.
        BMI와 비만도도 다시 계산한다.
        """

        record = self.search_by_id(patient_id)

        if record is None:
            return False

        if height <= 0 or weight <= 0:
            return False

        record.height = height
        record.weight = weight

        # BMI 다시 계산
        record.bmi = self.calculate_bmi(height, weight)

        # 비만도 다시 계산
        record.status = self.calculate_status(record.bmi)

        return True

    # 건강정보 삭제
    def delete_record(self, patient_id):
        """
        식별번호를 이용하여 건강정보를 삭제한다.
        """

        record = self.search_by_id(patient_id)

        if record is None:
            return False

        self.records.remove(record)

        return True

    # 건강정보 통계
    def get_statistics(self):
        """
        전체 인원수와 키, 몸무게, BMI의
        평균 및 표준편차를 계산한다.
        """

        count = len(self.records)

        if count == 0:
            return None

        heights = []
        weights = []
        bmis = []

        for record in self.records:
            heights.append(record.height)
            weights.append(record.weight)
            bmis.append(record.bmi)

        # 평균 계산
        avg_height = sum(heights) / count
        avg_weight = sum(weights) / count
        avg_bmi = sum(bmis) / count

        # 표준편차 계산 (모집단 기준)
        height_sd = (
            sum((x - avg_height) ** 2 for x in heights) / count
        ) ** 0.5

        weight_sd = (
            sum((x - avg_weight) ** 2 for x in weights) / count
        ) ** 0.5

        bmi_sd = (
            sum((x - avg_bmi) ** 2 for x in bmis) / count
        ) ** 0.5

        # 통계 결과 반환
        statistics = {
            "count": count,
            "avg_height": round(avg_height, 2),
            "avg_weight": round(avg_weight, 2),
            "avg_bmi": round(avg_bmi, 2),
            "height_sd": round(height_sd, 2),
            "weight_sd": round(weight_sd, 2),
            "bmi_sd": round(bmi_sd, 2)
        }

        return statistics


# 콘솔 프로그램
def main():

    manager = HealthManager()

    while True:

        print("\n-------- 건강정보 관리 시스템 --------")
        print("1. 건강정보 추가")
        print("2. 건강정보 목록 조회")
        print("3. 검색 및 상세조회")
        print("4. 건강정보 수정")
        print("5. 건강정보 삭제")
        print("6. 건강정보 통계")
        print("0. 종료")

        choice = input("메뉴를 선택하세요: ")

        # 1. 건강정보 추가
        if choice == "1":

            name = input("이름: ")

            try:
                birth_year = int(input("출생년도: "))
                gender = input("성별: ")
                height = float(input("키(cm): "))
                weight = float(input("몸무게(kg): "))

                if height <= 0 or weight <= 0:
                    print("키와 몸무게는 0보다 커야 합니다.")
                    continue

                result = manager.add_record(
                    name, birth_year, gender, height, weight
                )

                if result:
                    print("건강정보가 추가되었습니다.")
                else:
                    print("건강정보 추가에 실패했습니다.")

            except ValueError:
                print("숫자를 올바르게 입력해주세요.")

        # 2. 전체 목록 조회
        elif choice == "2":

            records = manager.get_all_records()

            if len(records) == 0:
                print("등록된 건강정보가 없습니다.")

            else:
                print("\n[건강정보 목록]")

                for record in records:
                    print("--------------------------------")
                    print("식별번호:", record.id)
                    print("이름:", record.name)
                    print("키:", record.height)
                    print("몸무게:", record.weight)
                    print("BMI:", record.bmi)
                    print("비만도:", record.status)

        # 3. 검색 및 상세조회
        elif choice == "3":

            patient_id = input("검색할 식별번호: ")

            record = manager.search_by_id(patient_id)

            if record is None:
                print("해당 정보가 없습니다.")

            else:
                print("\n[상세 건강정보]")
                print("식별번호:", record.id)
                print("이름:", record.name)
                print("생년:", record.birth_year)
                print("성별:", record.gender)
                print("키:", record.height)
                print("몸무게:", record.weight)
                print("BMI:", record.bmi)
                print("비만도:", record.status)

        # 4. 건강정보 수정
        elif choice == "4":

            patient_id = input("수정할 식별번호: ")

            try:
                height = float(input("변경할 키(cm): "))
                weight = float(input("변경할 몸무게(kg): "))

                if height <= 0 or weight <= 0:
                    print("키와 몸무게는 0보다 커야 합니다.")
                    continue

                result = manager.update_record(
                    patient_id, height, weight
                )

                if result:
                    print("건강정보가 수정되었습니다.")
                else:
                    print("해당 정보가 없거나 수정에 실패했습니다.")

            except ValueError:
                print("숫자를 올바르게 입력해주세요.")

        # 5. 건강정보 삭제
        elif choice == "5":

            patient_id = input("삭제할 식별번호: ")

            result = manager.delete_record(patient_id)

            if result:
                print("건강정보가 삭제되었습니다.")
            else:
                print("해당 정보가 없습니다.")

        # 6. 통계 조회
        elif choice == "6":

            stats = manager.get_statistics()

            if stats is None:
                print("통계를 계산할 데이터가 없습니다.")

            else:
                print("\n[건강정보 통계]")
                print("전체 인원수:", stats["count"])
                print("평균 키:", stats["avg_height"])
                print("평균 몸무게:", stats["avg_weight"])
                print("평균 BMI:", stats["avg_bmi"])
                print("키 표준편차:", stats["height_sd"])
                print("몸무게 표준편차:", stats["weight_sd"])
                print("BMI 표준편차:", stats["bmi_sd"])

        # 0. 종료
        elif choice == "0":

            print("프로그램을 종료합니다.")
            break

        else:
            print("잘못된 메뉴입니다. 다시 선택해주세요.")


if __name__ == "__main__":
    main()
