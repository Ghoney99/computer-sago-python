#5.1 정수형 난수 리스트의 정렬 및 경과시간 측정

import random
import time

def genBigRandList(n):
    #리스트 생성
    L=[]
    #리스트 L의길이가 n이 될때까지 반복
    while len(L)<n:
        #0~n사이의 난수 생성
        num=random.randint(0,n-1)
        #리스트L에 중복된 숫자가 들어가지 않기 위한 조건문
        if num not in L:
            L.append(num)
    return L

def printListSample(L, per_line = 10, sample_lines = 2):
    #첫부분 출력
    #이중 for문
    #줄을 바꾸는 for문
    for j in range(sample_lines):
        #한줄을 출력하는 for문
        for i in range(per_line):
            #L[i+(j*per_line)]는 i번째에 위치한 리스트를 출력하고 줄이 바뀌면 (j*per_line)를 더해 그 다음줄을 출력
            print("{:7}".format(L[i+(j*per_line)]), end="")
        print()

    print(". . . . .")

    #마지막 부분 출력
    #마지막 부분 출력의 시작지점을 계산
    last_satrt = len(L)-per_line*sample_lines
    #줄을 바꾸는 for문
    for j in range(sample_lines):
        #L[i+(j*per_line)]는 last_satrt+i번째에 위치한 리스트를 출력하고 줄이 바뀌면 (j*per_line)를 더해 그 다음줄을 출력
        for i in range(per_line):
             print("{:7}".format(L[last_satrt+i+(j*per_line)]), end="")
        print()


#두 개의 리스트 L_left와 L_right를 정렬하여 병합하는 함수
def _merge(L_left, L_right):
    
    i, j = 0, 0
    merged = []
    # 두 리스트의 첫 원소부터 비교하면서 작은 값을 merged 리스트에 추가
    while i < len(L_left) and j < len(L_right):
        if L_left[i] < L_right[j]:
            merged.append(L_left[i])
            i += 1
        else:
            merged.append(L_right[j])
            j += 1
    # 한쪽 리스트가 모두 merged 리스트에 추가되면 남은 원소들을 모두 추가
    merged += L_left[i:]
    merged += L_right[j:]
    return merged


#병합 정렬을 수행하는 함수
def mergeSort(L):
    if len(L) <= 1:
        return L
    # 리스트를 절반으로 나누어 각각 병합 정렬 수행
    mid = len(L) // 2
    L_left = mergeSort(L[:mid])
    L_right = mergeSort(L[mid:])
    # 두 개의 정렬된 리스트를 병합하여 하나의 정렬된 리스트로 만듦
    merged = _merge(L_left, L_right)
    return merged

# (Application) Performance test of merge sorting
while True:
    print("\nPerformance test of merge sorting algorithm")
    size = int(input("Input size of random list L (0 to quit) = "))
    if size == 0:
        break
    L = genBigRandList(size)

    # testing MergeSorting
    print("\nBefore mergeSort of L :")
    printListSample(L, 10, 2)
    t1 = time.time()
    sorted_L = mergeSort(L)
    t2 = time.time()
    print("After mergeSort of L :")
    printListSample(sorted_L, 10, 2)
    time_elapsed = t2 - t1
    print("Merge sorting took {} sec".format(time_elapsed))
