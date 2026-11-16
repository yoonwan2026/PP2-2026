
# AI 사용 주석
# AI 종류: ChatGPT
# 사용 목적: 건강정보 관리 모듈의 기본 코드 작성 및 이해
# 사용한 사람: 윤완
# 사용 날짜: 2026-11-15

import os
import json
import csv
import pickle


# 1. 건강정보 한 명의 데이터를 저장하는 클래스
class HealthRecord:

    def __init__(self, id, name, birth_year, gender, height, weight, bmi, status):
        self.id = id
        self.name = name
        self.birth_year = birth_year
        self.gender = gender
        self.height = height
        self.weight = weight
        self.bmi = bmi
        self.status = status

    # 객체를 딕셔너리로 바꾸는 함수
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "birth_year": self.birth_year,
            "gender": self.gender,
            "height": self.height,
            "weight": self.weight,
            "bmi": self.bmi,
            "status": self.status
        }


# 2. 건강정보를 관리하는 클래스
class HealthManager:

    def __init__(self):
        self.records = []

        # data 폴더가 없으면 자동으로 만들기
        os.makedirs("data", exist_ok=True)

    # 3. 식별번호 만들기
    def make_id(self):
        number = len(self.records) + 1
        return f"P2026-{number:04d}"

    # 4. 새로운 건강정보 등록하기
    def add_record(self, name, birth_year, gender, height, weight, bmi, status):

        new_record = HealthRecord(
            self.make_id(), name, birth_year, gender,
            height, weight, bmi, status
        )

        self.records.append(new_record.to_dict())

        print("건강정보가 등록되었습니다.")


    # 5. 파일 저장하기
    def save_data(self, file_type):

        file_path = f"data/health_data.{file_type}"

        try:
            # JSON 저장
            if file_type == "json":
                with open(file_path, "w", encoding="utf-8") as file:
                    json.dump(self.records, file, ensure_ascii=False, indent=4)

            # CSV 저장
            elif file_type == "csv":
                with open(file_path, "w", newline="", encoding="utf-8-sig") as file:
                    writer = csv.DictWriter(file, fieldnames=self.records[0].keys())
                    writer.writeheader()
                    writer.writerows(self.records)

            # TXT 저장
            elif file_type == "txt":
                with open(file_path, "w", encoding="utf-8") as file:
                    for record in self.records:
                        file.write(",".join(map(str, record.values())) + "\n")

            # Pickle 저장
            elif file_type == "pkl":
                with open(file_path, "wb") as file:
                    pickle.dump(self.records, file)

            print("파일 저장이 완료되었습니다.")

        except (OSError, IndexError) as e:
            print("파일 저장 중 오류가 발생했습니다:", e)


    # 6. 파일 불러오기
    def load_data(self, file_type):

        file_path = f"data/health_data.{file_type}"

        try:
            # JSON 불러오기
            if file_type == "json":
                with open(file_path, "r", encoding="utf-8") as file:
                    self.records = json.load(file)

            # CSV 불러오기
            elif file_type == "csv":
                with open(file_path, "r", encoding="utf-8-sig") as file:
                    reader = csv.DictReader(file)
                    self.records = list(reader)

            # TXT 불러오기
            elif file_type == "txt":
                with open(file_path, "r", encoding="utf-8") as file:
                    self.records = []
                    for line in file:
                        data = line.strip().split(",")
                        self.records.append({
                            "id": data[0],
                            "name": data[1],
                            "birth_year": int(data[2]),
                            "gender": data[3],
                            "height": float(data[4]),
                            "weight": float(data[5]),
                            "bmi": float(data[6]),
                            "status": data[7]
                        })

            # Pickle 불러오기
            elif file_type == "pkl":
                with open(file_path, "rb") as file:
                    self.records = pickle.load(file)

            print("파일 불러오기가 완료되었습니다.")

        except FileNotFoundError:
            print("저장된 파일이 없습니다.")

        except (OSError, ValueError, KeyError, IndexError, json.JSONDecodeError, pickle.UnpicklingError) as e:
            print("파일을 읽는 중 오류가 발생했습니다:", e)
            
if __name__ == "__main__":

    # 1. 건강정보 입력
    manager = HealthManager()

    manager.add_record(
        "홍길동", 1995, "남",
        175.0, 72.5, 23.67, "과체중"
    )

    manager.add_record(
        "김영희", 1998, "여",
        162.0, 52.0, 19.81, "정상"
    )

    # 2. 입력한 원래 데이터 출력
    print("===== 원래 데이터 =====")
    print(manager.records)

    # 원래 데이터 따로 보관
    original_records = manager.records.copy()

    # 3. 4가지 파일로 저장하고 다시 불러오기
    for file_type in ["json", "csv", "txt", "pkl"]:

        print(f"\n===== {file_type} 파일 테스트 =====")

        # 파일 저장
        manager.save_data(file_type)

        # 새로운 관리자 객체 생성
        test_manager = HealthManager()

        # 파일 불러오기
        test_manager.load_data(file_type)

        # 불러온 데이터 출력
        print("불러온 데이터:")
        print(test_manager.records)

        # 원래 데이터와 비교
        if original_records == test_manager.records:
            print("검증 성공: 원래 데이터와 일치합니다.")
        else:
            print("검증 실패: 원래 데이터와 다릅니다.")