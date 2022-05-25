# [S/W 문제해결 기본] 1일차 - View

for i in range(1, 11):
    print("#"+str(i), end=' ')
    input()
    b = list(map(int, input().split()))
    cnt = 0
    for j in range(2, len(b) - 2):
        temp = b[j] - max(b[j-1], b[j-2], b[j+1], b[j+2])
        if temp > 0:
            cnt += temp
    print(cnt)