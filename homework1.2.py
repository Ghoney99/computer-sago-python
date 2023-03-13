#  Homewrok1.2
#  작성자 : 장지헌
#  작성일자 : 2023.03.0.
#  Turtle로 직사각형 그리기

import turtle   #turtle은 turtle을 사용하기위한 라이브러리

#Homework 문제 번호, 본인의 학번, 이름을 출력
print("Homework 1.2 Turtle drawing of a rectangle")
print("Dept: 컴퓨터공학과, St_ID:21812055, Name: 장지헌")

#width와 length를 입력 받기 위해서 input함수를 사용, end=""는 줄을 자동으로 바꾸지 않기 위해 삽입
print("width of rectangle = ",end="")
width = int(input())
print("length of rectangle = ",end="")
length = int(input())

#t는 turtle 객체, 객체를 생성
t=turtle.Turtle()
#t의 모양은 turtle
t.shape("turtle")
#그림이 그려지지 않도록 t를 up함
t.up()
#t가 그리기 위한 시작위치로 이동
t.goto(width/2,length/2)

#그림이 그려지도록 t를 down함
t.down()
#직사각형을 그리기 위해 각각 직사각형의 모든 꼭짓점을 오른쪽으로 돌며 이동
t.goto(width/2,-length/2)
t.goto(-width/2,-length/2)
t.goto(-width/2,length/2)
t.goto(width/2,length/2)

#그림이 그려지지 않도록 t를 up함
t.up()
#t가 중심에 위치하도록 0,0 좌표로 이동
t.goto(0,0)
