import random

def genRandList(L, size):
    #리스트 초기화
    L.clear()
    #리스트 L의길이가 n이 될때까지 반복
    while len(L)<size:
        #0~n사이의 난수 생성
        num=random.randint(0,size-1)
        #리스트L에 중복된 숫자가 들어가지 않기 위한 조건문
        if num not in L:
            L.append(num)
    

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

def shuffleList(L):
    #리스트의 원소들을 랜덤하게 뒤섞는다.
    random.shuffle(L)
