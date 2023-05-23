import numpy as np
from numba import jit
import time

@jit(nopython=True)
def selection_sort(arr):
    # 배열의 각 요소에 대해 반복합니다.
    for i in range(len(arr)):
        # 현재 요소를 최솟값으로 가정합니다.
        min_idx = i
        # 최솟값을 찾기 위해 현재 요소 다음부터 배열의 끝까지 반복합니다.
        for j in range(i+1, len(arr)):
            # 만약 현재 요소보다 작은 값이 있다면 최솟값을 해당 인덱스로 업데이트합니다.
            if arr[j] < arr[min_idx]:
                min_idx = j
        # 현재 요소와 최솟값을 교환합니다.
        arr[i], arr[min_idx] = arr[min_idx], arr[i]


@jit(nopython=True)
def quick_sort(arr, low, high):
    # 조건: 하한 인덱스가 상한 인덱스보다 작을 때
    if low < high:
        # 파티션 함수를 사용하여 피벗 인덱스를 얻습니다.
        pivot_index = partition(arr, low, high)
        # 피벗을 기준으로 좌측 부분 배열을 정렬합니다.
        quick_sort(arr, low, pivot_index)
        # 피벗을 기준으로 우측 부분 배열을 정렬합니다.
        quick_sort(arr, pivot_index + 1, high)


@jit(nopython=True)
def partition(arr, low, high):
    # 피벗을 첫 번째 요소로 선택합니다.
    pivot = arr[low]
    # i는 왼쪽에서 오른쪽으로 이동하는 인덱스로, low - 1로 초기화합니다.
    i = low - 1
    # j는 오른쪽에서 왼쪽으로 이동하는 인덱스로, high + 1로 초기화합니다.
    j = high + 1
    # 무한 루프를 시작합니다.
    while True:
        # i를 증가시키면서 피벗보다 작은 요소를 찾습니다.
        i += 1
        while arr[i] < pivot:
            i += 1
        # j를 감소시키면서 피벗보다 큰 요소를 찾습니다.
        j -= 1
        while arr[j] > pivot:
            j -= 1
        # i와 j가 교차하면 파티션을 완료하고 j를 반환합니다.
        if i >= j:
            return j
        # i와 j의 요소를 교환합니다.
        arr[i], arr[j] = arr[j], arr[i]


@jit(nopython=True)
def hybrid_sort_jit(array, ss_cutoff):
    if len(array) <= ss_cutoff: # 만약 배열의 길이가 ss_cutoff 이하이면 선택 정렬을 사용
        selection_sort(array)
    else: # 그렇지 않으면 퀵 정렬을 사용합니다.
        quick_sort(array, 0, len(array) - 1)
    # 정렬된 배열을 반환합니다.
    return array


test_size = 10000000  # 테스트용 배열의 크기
ss_cutoff_range = range(5, 36)  # 선택 정렬 임계값 범위
times = []  # 각 임계값에 대한 실행 시간을 저장할 리스트
# 최적의 ss_cutoff 찾기
for ss_cutoff in ss_cutoff_range:
    array = np.random.random(test_size) # 랜덤한 배열 생성
    start_time = time.time()    # 정렬 수행 시간 측정 시작
    hybrid_sort_jit(array, ss_cutoff)
    end_time = time.time()
    duration = end_time - start_time
    times.append(duration)  # 정렬 수행 시간 계산 및 리스트에 추가
optimal_ss_cutoff = ss_cutoff_range[np.argmin(times)]   # 실행 시간이 가장 짧은 ss_cutoff 값 찾기
print("Optimal ss_cutoff:", optimal_ss_cutoff)  # 최적의 ss_cutoff 값 출력


# Compare performance for different array sizes
array_sizes = [100000, 1000000, 10000000]

for size in array_sizes:
    array = np.random.random(size)

    # Hybrid Sort
    start_time = time.time()
    hybrid_sort_jit(array, optimal_ss_cutoff)
    end_time = time.time()
    hybrid_sort_duration = end_time - start_time

    # Numpy Sort
    start_time = time.time()
    np.sort(array)
    end_time = time.time()
    numpy_sort_duration = end_time - start_time

    print("Array Size:", size)
    print("Hybrid Sort Duration:", hybrid_sort_duration)
    print("Numpy Sort Duration:", numpy_sort_duration)
    print()
