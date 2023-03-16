#  Homewrok4.2
#  작성자 : 장지헌
#  작성일자 : 2023.03.16
# 튜플 응용 - Student

# Homework 4.2

# 난수 생성을 위한 라이브러리
import random

#튜플을 출력하기 위한 함수
def print_tuple(**student):
    for i in range(len(students)):
        print("student[{}] : name({}), st_id({}), major({}), GPA({})".format(i,students[i][0], students[i][1], students[i][2], students[i][3]))
    

# 리스트 생성
name = ["김광현", "에드먼", "김하성", "이정후", "박병호", 
        "김현수", "박건우", "강백호", "양의지", "최정"]
st_id = []
major = ["CE", "EE", "ICE", "ME", "ICE", "CE", "EE", "ME", "ME", "CE"]
gpa = []

# 학번 리스트에 랜덤으로 학번 생성 (11학번~23학번)
for i in range(10):
    st_id.append(random.randint(11000000, 23999999))

# 성적리스트에 랜덤으로 성적생성, 소수 두째자리까지만 표시 (0.00~4.50)
for i in range(10):
    gpa.append(round(random.uniform(0.00, 4.50), 2))

#zip을 이용해 각각의 리스트들을 students 튜플로 만든다.
students = list(zip(name, st_id, major, gpa))

print_tuple()
print()

#튜플을 오름차순으로 정렬 (별도의 정렬 기준 설정 없이)
students.sort()
print_tuple()
print()

#튜플을 오름차순으로 정렬 
students.sort(key=lambda x: x[3], reverse=True)
print_tuple()
