# [S/W 문제해결 응용] 4일차 - 보급로

import sys
from collections import deque

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
INF = 99999
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
T = int(input())

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    global minSum

    while queue:
        x, y = queue.popleft()
        if x == N-1 and y == N-1:   # 도착지 도착했다고 return하면 안된다!! 더 최소가 나올 수 있기 때문.. 결국 다 해봐야 한다! 노타빌리티에 정리해놓음..
            if minSum > result[N-1][N-1]:
                minSum = result[N-1][N-1]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue

            if result[x][y] + _map[nx][ny] < result[nx][ny]:
                result[nx][ny] = result[x][y] + _map[nx][ny]
                queue.append((nx, ny))

for t in range(1, T+1):
    N = int(input())
    _map = [list(map(int, input().rstrip())) for _ in range(N)]
    result = [[INF]*N for _ in range(N)]    # result[x][y]: x, y까지 고려했을 때 최소 복구 시간!
    result[0][0] = 0
    minSum = INF
    bfs(0, 0)
    print(f"#{t} {minSum}")