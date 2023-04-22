import time

# memoization을 위한 빈 딕셔너리 생성
memo = dict()

#n번째 피보나치 수열을 계산하는 재귀함수 (memoization 적용)
def dynFibo(n):
    #이미 계산된 값인 경우
    if n in memo:
        return memo[n]
    
    #n이 0이나 1인경우
    elif n <= 1:
        #메모에 저장
        memo[n] = n
        return n
    
    #n이 2이상인 경우
    else:
        #n-1번째와 n-2번째를 재귀호출하여 계산
        fibo_n = dynFibo(n-1) + dynFibo(n-2)
        #메모에 저장
        memo[n] = fibo_n
        return fibo_n
    
(start, stop, step) = tuple(map(int, input("input start, stop, step of Fibonacci series : ").split(' ')))

for n in range(start ,stop+1 ,step):
    start_time= time.time() # 호출 및 경과시간의 시작시간
    fibo_n = dynFibo(n)     # 함수 동작
    end_time = time.time()  # 호출 및 경과시간의 종료시간
    t_elapse_us = end_time - start_time  #종료시간과 시작시간의 차를 이용해 실행시간 측정
    print("dynFibo({:3d}) = {:25d}, took {:10.2f}[micro_sec]".format(n, fibo_n, t_elapse_us))
