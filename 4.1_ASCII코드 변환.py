#  Homewrok4.1
#  작성자 : 장지헌
#  작성일자 : 2023.03.16
#  ASCII 코드표로 부터 숫자 (‘0’~’9’), 알파벳 대문자 (‘A’~’Z’), 알파벳 소문자 (‘a’~’z’) 추출 및 리스트 생성, 출력

#Homework 4.1

# 리스트 생성
L_digits = []
L_upper = []
L_lower = []

#ord() 함수를 사용해 문자를 아스키코드로 바꾸어 반복문을 실행
#리스트에 추가할때는 chr()함수를 이용하여 아스키코드를 문자로 변경
for i in range(ord("0"), ord("9")+1):
    L_digits.append(chr(i))

for i in range(ord("A"), ord("Z")+1):
    L_upper.append(chr(i))

for i in range(ord("a"), ord("z")+1):
    L_lower.append(chr(i))

#출력
print("L_digits (size: {}) : {}".format(len(L_digits), L_digits))
print("L_upper (size: {}) : {}".format(len(L_upper), L_upper))
print("L_lower (size: {}) : {}".format(len(L_lower), L_lower))
