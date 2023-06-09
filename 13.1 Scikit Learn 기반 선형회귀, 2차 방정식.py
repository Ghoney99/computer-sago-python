# 13.1 Scikit Learn 기반 선형회귀, 2차 방정식
# Author : 장지헌
# Date : 2023. 6. 7.
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

# 데이터 생성
x = np.linspace(-50.0, 50.0, 100) # -50부터 50까지 100개의 데이터 생성
y = x**2 - 10*x - 200 # 2차 방정식 y = x^2 - 10x - 200

# 잡음 생성
mu, sigma = 0.0, 100.0 # 잡음의 평균과 표준편차 설정
noise = np.random.normal(mu, sigma, x.size) # 잡음 생성
y_noise = y + noise # 잡음이 추가된 데이터 생성

# 선형 회귀 모델 피팅
poly = PolynomialFeatures(degree=2, include_bias=False) # 2차 다항식 특성 생성기 생성
x_poly = poly.fit_transform(x[:, np.newaxis]) # x를 2차 다항식으로 변환
reg = LinearRegression().fit(x_poly, y_noise) # 다항 회귀 모델 피팅
y_pred = reg.predict(x_poly) # 예측값 계산

# 그래프 표현
plt.scatter(x, y_noise, color='b', label='y_noise') # 잡음이 추가된 데이터를 산점도로 표현
plt.plot(x, y_pred, color='r', label='y_pred') # 예측된 곡선을 선 그래프로 표현
plt.xlabel('x') # x축 레이블 설정
plt.ylabel('y') # y축 레이블 설정
plt.title('y_noise = +1.00*x**2-200.00+noise') # 그래프 제목 설정
plt.legend() # 범례 표시
plt.show() # 그래프 출력

