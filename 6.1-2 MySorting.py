def selectionSort(L):
    # 리스트의 모든 원소를 순회
    for i in range(len(L)):
        # 현재 위치부터 끝까지 가장 작은 원소의 인덱스를 찾음
        min_idx = i
        for j in range(i+1, len(L)):
            if L[j] < L[min_idx]:
                min_idx = j
        # 현재 위치와 가장 작은 원소를 교환
        L[i], L[min_idx] = L[min_idx], L[i]


def mergeSort(L):

    if len(L) > 1:
        # 리스트를 중간 지점을 기준으로 둘로 나눔
        mid = len(L)//2
        L_left = L[:mid]
        L_right = L[mid:]

        # 재귀적으로 각 부분 리스트를 병합 정렬을 수행
        mergeSort(L_left)
        mergeSort(L_right)

        i = j = k = 0
        # 두 부분 리스트의 첫번째 원소부터 비교하여 작은 원소를 병합
        while i < len(L_left) and j < len(L_right):
            if L_left[i] < L_right[j]:
                L[k] = L_left[i]
                i += 1
            else:
                L[k] = L_right[j]
                j += 1
            k += 1

        # 아직 처리하지 못한 나머지 원소들을 처리
        while i < len(L_left):
            L[k] = L_left[i]
            i += 1
            k += 1

        while j < len(L_right):
            L[k] = L_right[j]
            j += 1
            k += 1

    # 최종적으로 정렬된 리스트 반환
    return L
