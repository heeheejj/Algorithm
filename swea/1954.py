# 달팽이 숫자

t = int(input())
dx = [0, 1, 0, -1]  # 우 -> 하 -> 좌 -> 상
dy = [1, 0, -1, 0]

for i in range(t):
    n = int(input())

    snail = [[0] * n for _ in range(n)]

    nx, ny = 0, 0   # 처음 위치 0,0
    dir = 0         # 초기 방향 설정(오른쪽부터)

    for j in range(1, n*n+1):
        snail[nx][ny] = j

        nx += dx[dir]
        ny += dy[dir]

        if nx < 0 or ny < 0 or nx >= n or ny >= n or snail[nx][ny] != 0:
            nx -= dx[dir]   # 위에서 해준 연산 취소
            ny -= dy[dir]
            dir = (dir + 1) % 4     # 방향 재설정
            nx += dx[dir]   # 다시 연산
            ny += dy[dir]

    print("#"+str(i+1))
    for j in range(n):
        for k in range(n):
            print(snail[j][k], end=' ')
        print()