mon_day = {1: 31, 3: 31, 5: 31, 7: 31, 8: 31,
           10: 31, 12: 31, 4: 30, 6: 30, 9: 30, 11: 30}

month_name = {1: "Januaey", 2: "Feburary", 3: "March", 4: "April", 5: "May", 6: "Jun", 7: "July ",
              8: "August", 9: "September", 10: "Octorber", 11: "November", 12: "December"}

day_name = ["SUN", "MON", "TUE", "WED", "THR", "FRI", "SAT"]

# 윤년 계산 함수
def is_leap(year):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return True
    else:
        return False

# 시작일 계산 함수
def first_day(year, month):
    total_day = 0
    #윤년이면 366를 시작일에 더해준다./ 평년이면 365를 더해준다.
    for y in range(1900, year):
        if is_leap(y):
            total_day += 366
        else:
            total_day += 365
    #달을 더해준다. (예 : 1월이면 31, 4월이면 30일을 더해준다.)
    for m in range(1, month):
        total_day += mon_day[m]
    return total_day % 7 + 1

#달력 출력 함수
def calendar(year, month, day):
    print("{} of Year {}".format(month_name[month], year))
    print("===========================")
    #SUN MON TUE WED THR FRI SAT를 출력
    for d in day_name:
        print(d,end=" ")
    print()

    print("---------------------------")
    #달의 첫날앞에 공백을 생성
    for d in range(0, first_day(year, month)%7):
        print("    ", end="")
    #날짜를 출력
    for d in range(1, mon_day[month]+1):
        #공백포함 문자열의 길이가 4이 되도록 출력
        print("{:3d} ".format(d), end="")
        #일주일이 지나면 줄바꿈
        if (d + first_day(year, month)) % 7 == 0:
            print()
    if (d + first_day(year, month)) % 7 != 0:
        print()
    print("===========================")

year, month, day = map(int, input("연도, 월, 일을 입력하시오 (예 : 2023 01 01) : ").split())
print("입력된 연도, 월, 일 : {}. {}. {}".format(year, month, day))
print()

# 윤년을 계산 후, 딕셔너리에 추가
if is_leap(year) == True:
    mon_day[2] = 29
else:
    mon_day[2] = 28

# 달력 출력
calendar(year, month, day)
