# Homework 12.1 A Dynamic Programming solution for Rod cutting problem (1)
INT_MIN = -32767

def printLPrices(L_p):
    print("length :", end='')  # 길이 라벨 출력
    for i in range(len(L_p)):
        print("{:3d}".format(i+1), end=', ')  # 길이 출력
    print("\nprice :", end='')  # 가격 라벨 출력
    for i in range(len(L_p)):
        print("{:3d}".format(L_p[i]), end=', ')  # 가격 출력
    print()

def printLCuttings(L_p, L_cuttings):
    print("selected cuttings : ", end='')  # 선택된 자르기 출력
    for i in range(len(L_cuttings)):
        print("[length({}) : price({})]".format(L_cuttings[i]+1, L_p[L_cuttings[i]]), end='')  # 선택된 자르기의 길이와 가격 출력
    print()


# cutRod() finds the best obtainable revenue from a rod of length max_len and
# price[] as prices of different pieces
# cuttings[i] contains the selected cutting for maximum profit with length i
def cutRod(price, max_len):
    val = [0] * (max_len+1)  # 각 길이에 대한 최대 수익을 저장하는 배열
    cuttings = [[] for _ in range(max_len+1)]  # 각 길이에 대한 최적 자르기를 저장하는 배열
    val[0] = 0  # 길이가 0인 경우 수익은 0

    for i in range(1, max_len+1):
        max_val = -float('inf')  # 최대 수익 초기화
        for j in range(i):
            # 길이 i를 자르는 경우의 수익과 이전 길이에 대한 최대 수익의 합을 비교하여 최대값 갱신
            if price[j] + val[i-j-1] > max_val:
                max_val = price[j] + val[i-j-1]
                # 현재 자르는 위치 j를 선택한 최적 자르기를 저장
                cuttings[i] = [j] + cuttings[i-j-1]
        val[i] = max_val  # 길이 i에 대한 최대 수익 저장

    return val[max_len], cuttings[max_len]


# Homework 12.1 A Dynamic Programming solution for Rod cutting problem (2)
if __name__ == "__main__":
    L_pr_a = [1, 5, 8, 9, 10, 17, 18, 20]
    L_pr_b = [2, 5, 8, 11, 14, 17, 20, 23]
    L_pr_c = [3, 5, 8, 11, 14, 17, 20, 23]
    for L_name, L_p in [("case A", L_pr_a), ("case_B", L_pr_b), ("case_C", L_pr_c)]:
        print(L_name)
        printLPrices(L_p)
        max_len = len(L_p)
        max_rev, L_cuttings = cutRod(L_p, max_len)
        print("Maximum Obtainable Value with max length ({}) = {}".format(max_len, max_rev))
        printLCuttings(L_p, L_cuttings)