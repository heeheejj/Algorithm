# [S/W 문제해결 기본] 2일차 - Sum

for _ in range(1, 11):
    print("#"+input(), end=' ')
    arr = list()
    sums = list()   # 행, 열, 대각선의 합을 담는 리스트 (행의 합인지 열의 합인지 구분 불필요)
    for i in range(100):
        row = list(map(int, input().split()))
        rowSum = sum(row)
        sums.append(rowSum)   # 각 행의 합 리스트에 추가
        arr.append(row)         # 각 행을 담을 리스트를 arr의 원소로 추가 (arr는 2차원 리스트가 됨)
    dgsSum1 = 0
    dgsSum2 = 0
    for j in range(100):
        colSum = 0
        for i in range(100):
            colSum += arr[i][j]
            if i == j:
                dgsSum1 += arr[i][j]
            if i == 4 - j:
                dgsSum2 += arr[i][j]
        sums.append(colSum)
    sums.append(dgsSum1)
    sums.append(dgsSum2)
    print(max(sums))