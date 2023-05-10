# HW 10.1 정렬 함수의 성능 비교 - mergeSort(), NumPy sort()
# Author : 장지헌
# Date : 2023. 5. 10.

import random

def genRandList(size):
    L = []
    #리스트 L의길이가 n이 될때까지 반복
    L = random.sample(range(0, size), size)
    return L
    

def printListSample(L, per_line = 10, sample_lines = 2):
    #첫부분 출력
    #이중 for문
    #줄을 바꾸는 for문
    for j in range(sample_lines):
        #한줄을 출력하는 for문
        for i in range(per_line):
            #L[i+(j*per_line)]는 i번째에 위치한 리스트를 출력하고 줄이 바뀌면 (j*per_line)를 더해 그 다음줄을 출력
            print("{:8}".format(L[i+(j*per_line)]), end="")
        print()

    print(". . . . .")

    #마지막 부분 출력
    #마지막 부분 출력의 시작지점을 계산
    last_satrt = len(L)-per_line*sample_lines
    #줄을 바꾸는 for문
    for j in range(sample_lines):
        #L[i+(j*per_line)]는 last_satrt+i번째에 위치한 리스트를 출력하고 줄이 바뀌면 (j*per_line)를 더해 그 다음줄을 출력
        for i in range(per_line):
             print("{:8}".format(L[last_satrt+i+(j*per_line)]), end="")
        print()

def shuffleList(L):
    #리스트의 원소들을 랜덤하게 뒤섞는다.
    random.shuffle(L)