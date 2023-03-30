def printMtrx(name, M):
    #행렬의 이름 출력
    print("{} = ".format(name))
    
    #이중for문을 통해 2차원배열에서 1차원 배열만 추출
    for L in M:
        #1차원 배열의 원소들을 출력
        for element in L:
            print("{:2}".format(element) , end=" ")
        print()

def addMtrx(M1, M2):
    # 행렬의 크기가 다를 때 오류 메세지 출력
    if len(M1) != len(M2) or len(M1[0]) != len(M2[0]):
        print("add를 수행할 수 없습니다.")
        return None

    #add 진행
    result = []
    # 이중 for문을 진행
    for i in range(len(M1)):
        #result에 들어갈 lsit인 row 생성
        row = []
        #덧셈 계산
        for j in range(len(M1[0])):
            row.append(M1[i][j] + M2[i][j])
        result.append(row)
    return result

def subMtrx(M1, M2):
    # 행렬의 크기가 다를 때 오류 메세지 출력
    if len(M1) != len(M2) or len(M1[0]) != len(M2[0]):
        print("add를 수행할 수 없습니다.")
        return None

    #sub 진행
    result = []
    # 이중 for문을 진행
    for i in range(len(M1)):
        #result에 들어갈 lsit인 row 생성
        row = []
        #뺄셈 계산
        for j in range(len(M1[0])):
            row.append(M1[i][j] - M2[i][j])
        result.append(row)
    return result

def mulMtrx(M1, M2):
    #M1의 열의 개수와 M2의 행의 개수가 같지 않은 경우
    if len(M1[0]) != len(M2):
        print("곱셈이 불가능한 행렬입니다.")
        return None

    #곱셈계산
    result = [[0]*len(M2[0]) for _ in range(len(M1))]
    for i in range(len(M1)):
        for j in range(len(M2[0])):
            for k in range(len(M2)):
                result[i][j] += M1[i][k] * M2[k][j]

    return result
