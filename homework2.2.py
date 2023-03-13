#  Homewrok2.2
#  작성자 : 장지헌
#  작성일자 : 2023.03.10
#  실수 자료형 데이터 입력 및 통계 분석

#Homework 2.2

# 통계 분석을 위해 NumPy 모듈을 import
import numpy as np

# data라는 list를 생성
data = []

#입력받은 데이터들을 입력받고 공백을 기준으로 split하여 data에 저장
#이때 입력 받은 데이터들은 float형으로 저장
data = list(map(float, input("실수 10개를 입력하시오").split()))

#format함수를 사용하여 data 리스트의 원소들을 출력
print("데이터 = {}".format(data))

#Numpy의 메소드를 사용하여 평균, 분산, 표준편차를 계산
#np.mean은 평균, np.var은 분산, np.std은 표준편차를 구하는 메소드이다.
print("평균 = {}, 분산 = {}, 표쥰편차 = {}".format(np.mean(data), np.var(data), np.std(data)))

