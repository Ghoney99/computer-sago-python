class Person:
    def __init__(self, name, age):
        self.name = name  # 인스턴스 변수 name에 인자 name을 할당합니다.
        self.age = age  # 인스턴스 변수 age에 인자 age를 할당합니다.

        # 만약 입력받은 age가 0보다 작거나 100보다 크다면, 에러 메시지를 출력하고 
        # age를 0으로 초기화합니다.
        if age > 100 or age<0:
            print(f"***ERROR in setting age(name:{name}, age:{age})")
            self.age = 0
        else:
            self.age = age

#Student클래스는 Person클래스을 상속받음
class Student(Person):
    #생성자(init)에서는 부모 클래스의 
    #생성자(super().init)를 호출하여 이름(name)과 나이(age)를 초기화
    def __init__(self, name, age, st_id, major, gpa):
        super().__init__(name, age)
        self.st_id = st_id
        self.major = major
        self.gpa = gpa

        # 학번이 음수인 경우, 오류 메시지 출력 후 st_id를 0으로 설정
        if st_id < 0:
            print(f"***ERROR in setting st_id(name:{name}, age:{age})")
            self.st_id = 0
        else:
            self.st_id = st_id

        # 전공이 주어진 범위에 해당하지 않는 경우, 오류 메시지 출력 후 major를 "None"으로 설정
        if major not in ["ICE", "ME", "EE", "CE", "SE"]:
            print(f"***ERROR in setting major(name:{name}, age:{age})")
            self.major = "None"
        else:
            self.major = major

        # gpa가 0~4.5 범위를 벗어난 경우, 오류 메시지 출력 후 gpa를 0으로 설정
        if gpa < 0 or gpa > 4.5:
            print(f"***ERROR in setting gpa(name:{name}, age:{age})")
            self.gpa = 0
        else:
            self.gpa = gpa
    
    def __str__(self):
        return f"Student({self.name}, {self.age}, {self.st_id}, {self.major}, {self.gpa})"

	#두 학생(st1, st2)을 비교하여 정렬 기준(key)에 따라 순서를 결정하는 함수
	def compareStudent(st1, st2, key):

    	#key 값이 "st_id"인 경우, st_id 값을 기준으로 작은 값이 우선
    	if key == "st_id":
        	if st1.st_id < st2.st_id:
            	return True
        	else:
            	return False
        
	    #key 값이 "name"인 경우, name 값을 기준으로 알파벳 순서가 우선
	    elif key == "name":
	        if st1.name < st2.name:
	            return True
	        else:
	            return False
        
	    #key 값이 "age"인 경우, age 값을 기준으로 작은 값이 우선
	    elif key == "age":
	        if st1.age < st2.age:
	            return True
	        else:
	            return False
        
 	   #key 값이 "major"인 경우, major 값을 기준으로 ["ICE", "ME", "EE", "CE", "SE"]에 있는지 판단
 	   elif key == "major":
 	       if st1.major < st2.major:
 	           return True
 	       else:
 	           return False
 	       
	    #key 값이 "GPA"인 경우, gpa 값을 기준으로 큰 값이 우선
	    elif key == "GPA":
	        if st1.gpa > st2.gpa:
	            return True
	        else:
	            return False

	def sortStudent(L_st, key):
	    for i in range(0, len(L_st)):
	        min_idx = i
	        for j in range(i+1, len(L_st)):
	            if compareStudent(L_st[j], L_st[min_idx], key):
	                min_idx = j
 	       if min_idx != i:
 	           L_st[i], L_st[min_idx] = L_st[min_idx], L_st[i]

	def printStudents(L_st):
	    for s in range(len(L_st)):
	        print(L_st[s])



if __name__ == "__main__":
    students = [
        Student("Kim", 21, 12345, "EE", 4.0),
        Student("Lee", 22, 11234, "ME", 4.2),
        Student("Park", 20, 10234, "ICE", 4.3),
        Student("Hong", 19, 13123, "CE", 4.1),
        Student("Yoon", 23, 11321, "ICE", 4.2),
        Student("Wrong", 250, 15321, "??", 3.2),
        Student("Alpha", 18, 10111, "CS", 4.4),
	Student("Zedai", 19, 10222, "ICE", 4.4),
	Student("Beta", 20, 11333, "SE", 3.9),
	Student("Oliver", 21, 12555, "CE", 3.8)]
    ]
    
    print("students before sorting:")
    printStudents(students)
    
    sortStudent(students, "name")
    print("\nstudents after sorting by name:")
    printStudents(students)
    
    sortStudent(students, "st_id")
    print("\nstudents after sorting by student_id:")
    printStudents(students)
    
    sortStudent(students, "GPA")
    print("\nstudents after sorting by GPA in decreasing order:")
    printStudents(students)
