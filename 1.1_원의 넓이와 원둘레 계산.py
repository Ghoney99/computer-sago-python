#  Homewrok1.1
#  작성자 : 장지헌
#  작성일자 : 2023.03.0.
#  원의 넓이와 원둘레 계산

import math #원주율을 사용하기 위한 math 라이브러리

#Homework 문제 번호, 본인의 학번, 이름을 출력
print("Homework 1.1 Calculation of area circumference of a circle")
print("Dept: 컴퓨터공학과, St_ID:21812055, Name: 장지헌")

radius = 1

#무한 반복을 하기 위한 while문
while(1):
    #반지름을 입력 받기 위해서 input함수를 사용, end=""는 줄을 자동으로 바꾸지 않기 위해 삽입
    print("input radius of circle = ",end="")

    #input함수로 입력을 받으면 문자열형태로 입력을 받기때문에 int()를 사용하여 정수형태로 바꾸어줌
    radius = int(input())

    #입력받은 반지름이 0이면 반복문 종료
    if(radius==0):
        break

    #원의 넓이 공식과 원둘레 공식
    #math.pi는 math 라이브러리를 사용하여 원주율을 나타냄
    area = math.pi*radius*radius
    circumference = math.pi*2*radius

    #.format()으로 radius, area, circumference 변수를 출력한다.
    print("circle of radius ({}) : area ({}), circumference ({})".format(radius, area, circumference))
