# [S/W 문제해결 기본] 1일차 - Flatten

for i in range(1, 11):
    print("#"+str(i), end=' ')

    dumpCnt = int(input())
    heights = list(map(int, input().split()))

    for _ in range(dumpCnt):
        M, m = 0, 0
        M = max(heights)
        m = min(heights)
        if M - m <= 1:
            break

        heights[heights.index(M)] -= 1
        heights[heights.index(m)] += 1
    print(max(heights) - min(heights))