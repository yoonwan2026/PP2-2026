# =====================================================
# 작성자 : 윤완
# 작성일 : 2026-10-13
# 문제   : 06. 학과(Department), 교과목(Course), 학생(Student) - has-a 관계
# 설계   : 1) Department는 학과 이름과 course_list(교과목 목록)를 가진다.
#             add_course()는 Course를 만들어 목록에 넣고 그 Course를 돌려준다.
#          2) Course는 교과목 이름, 학점, student_list(수강생 목록)를 가진다.
#          3) Student는 이름, 학번, my_courses(수강 과목 목록)를 가진다.
#             enroll()을 하면 학생의 수강 목록과 교과목의 수강생 목록에 서로 추가한다.
# =====================================================


class Course:
    def __init__(self, name, credit):
        self.name = name
        self.credit = credit
        self.student_list = []  


class Department:
    def __init__(self, name):
        self.name = name
        self.course_list = [] 

    def add_course(self, course_name, credit):
        new_course = Course(course_name, credit)
        self.course_list.append(new_course)
        return new_course


class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.my_courses = []  

    def enroll(self, course):
        self.my_courses.append(course)
        course.student_list.append(self)


dept = Department("컴퓨터") 
math1 = dept.add_course("공업수학", 3)  
math2 = dept.add_course("이산수학", 2)

kim = Student("Kim", 20200001) 
kim.enroll(math1)

print(dept.name, "학과의 교과목 수 :", len(dept.course_list))
print(kim.name, "학생이 듣는 과목 :", kim.my_courses[0].name)
print(math1.name, "수강생 수 :", len(math1.student_list))