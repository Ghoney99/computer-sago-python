# HW 11.2 정규분포함수의 특성 분석
# Author : 장지헌
# Date : 2023. 5. 16

import numpy as np
import matplotlib.pyplot as plt

# 평균(mu)과 표준편차(sigma)가 주어진 배열/리스트 x에 대해 정규 분포 값을 계산하여 배열/리스트 Y를 생성하여 반환하는 함수
def gauss(mu, sigma, x):
    y = 1.0 / (sigma * np.sqrt(2 * np.pi)) * np.exp(-((x - mu) ** 2) / (2 * sigma ** 2))
    return y

# 사용자 입력에 따라 정규 분포 그래프를 생성하고 표시하는 메인 함수입
def main():
    X = np.linspace(-8, 8, 100)  # -8 ~ +8 구간을 100개의 등 간격으로 나누는 리스트 X를 생성

    menu = int(input("메뉴를 선택하세요 (1 또는 2): "))

    if menu == 1:  # 1일때, 실행
        mus = [0.0]  # mu 값들을 리스트로 저장
        sigmas = [0.5, 1.0, 2.0]  # sigma 값들을 리스트로 저장

        for mu in mus:
            plt.figure()  # Matplotlib에서 새로운 그림(figure)을 생성하는 함수
            for sigma in sigmas:  # sigmas 리스트에 있는 각각의 값을 순회하면서 반복 실행하는 반복문
                Y = gauss(mu, sigma, X)
                plt.plot(X, Y, label=f"sigma={sigma}")
            plt.title(f"Nomal Distribution Graph 1 - mu={mu}, sigma={sigmas}")  # 그래프 제목
            plt.legend()  # 그래프에 범례(legend)를 표시하는 함수
            plt.xlabel("X")
            plt.show()  # 그래프 출력

            print(f"mu={mu} 일 때, sigma 값이 달라질 때의 변화:\n")
            print("sigma 값이 작을수록 평균 주변에서의 확률이 높아집니다.")
            print("sigma 값이 클수록 분포의 폭이 넓어집니다.")

    elif menu == 2:  # 2일때, 실행
        sigma = 1.0  # 고정된 sigma 값
        mus = [-2.0, 0.0, 2.0]  # mu 값들을 리스트로 저장

        for mu in mus:
            Y = gauss(mu, sigma, X)
            plt.plot(X, Y, label=f"mu={mu}")

        plt.title(f"Nomal Distribution Graph 2 - mu={mus}, sigma={sigma}")  # 그래프 제목
        plt.legend()  # 그래프에 범례(legend)를 표시하는 함수
        plt.xlabel("X")
        plt.show()  # 그래프 출력

        print(f"sigma={sigma} 일 때, mu 값이 달라질 때의 변화:\n")
        print("mu 값이 작을수록 분포의 중심이 왼쪽으로 이동합니다.")
        print("mu 값이 클수록 분포의 중심이 오른쪽으로 이동합니다.")
    else:
        print("잘못된 메뉴를 선택하셨습니다.")

if __name__ == "__main__":
    main()
