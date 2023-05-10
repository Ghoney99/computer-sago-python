# HW 10.2 NumPy 확장 모듈을 사용한 선형 시스템 해 (solution) 산출
# Author : 장지헌
# Date : 2023. 5. 10.

import numpy as np  # numpy 모듈 import
#------------------------------------------
def main():
    # 선형시스템 AX = B에서 A와 B의 준비
    A = np.array([[1, 5, 3, 3, 7],
                [3, 4, 5, 6, 7],
                [1, 3, 5, 7, 9],
                [3, 1, 4, 1, 5],
                [5, 5, 3, 3, 1]])  # numpy 배열 A 생성
    B = np.array([105, 135, 145, 74, 75])  # numpy 배열 B 생성

    # 배열 A 출력
    print("A = \n", A)

    # 배열 B 출력
    print("B = \n", B)

    # 배열 A의 행렬식(det_A) 계산 및 출력
    det_A = np.linalg.det(A)
    print("det_A:\n", det_A)

    # 배열 A의 역행렬(inv_A) 계산 및 출력
    inv_A = np.linalg.inv(A)
    print("inv_A:\n", inv_A)

    # 선형시스템 AX = B의 해 (solution)인 X의 산출 및 출력
    X = np.linalg.solve(A, B)
    print("X = \n", X)

    # B1 = A * X의 계산 및 B1 출력
    B1 = np.matmul(A, X)
    print("B1 = A * X =\n", B1)

    # X1 = inv_A * B의 계산 및 X1 출력
    X1 = np.matmul(inv_A, B)
    print("X1 = inv_A * B:\n", X1)

if __name__ == "__main__":
    main()