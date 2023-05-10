# HW 10.3 NumPy 기반 행렬 연산
# Author : 장지헌
# Date : 2023. 5. 10.

import numpy as np

# 데이터 입력
data = np.loadtxt("matrix_7x7_data.txt")

# 2차원 ndarray A 생성
A = np.array(data)
print("A =\n", A)

# 배열 A의 행렬식(det_A) 계산 및 출력
det_A = np.linalg.det(A)
print("det_A:\n", det_A)

# 역행렬 A_inv 생성
A_inv = np.linalg.inv(A)
print("A_inv =\n", A_inv)

# 행렬 곱셈 E = A × A_inv 계산
E = np.matmul(A, A_inv)
print("E = np.matmul(A, A_inv) = \n", E)

