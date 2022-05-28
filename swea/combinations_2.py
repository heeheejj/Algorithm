

# 주석 없는 ver (재귀)
def combinations2(lst, k):
    if k == 0:
        return [[]]
    arr = []
    for x in range(0, len(lst)):
        m = lst[x]
        _lst = lst[x+1:]
        for p in combinations2(_lst, k-1):
            arr.append([m]+p)
    return arr

# 주석 ver (재귀)
def combinations3(lst, k):
    if k == 0:
        return [[]]
    arr = []    # 결과 리스트
    for x in range(0, len(lst)):    # lst 길이만큼 반복
        m = lst[x]  # 리스트의 현재 원소 기억
        _lst = lst[x+1:]    # 리스트에서 현재 원소 이후부터 다시 리스트 만들기
        for p in combinations3(_lst, k-1):   # 새로 만든 리스트에서 k-1만큼 지금 이 함수 재귀호출
            arr.append([m]+p)   # arr에 현재원소 + 나머지
    return arr