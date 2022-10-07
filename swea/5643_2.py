# [Professional] 키 순서
# graph: 화살표 방향이 키 더 작은애 -> 키 더 큰애
# 메모리 오류남
import sys
from collections import deque
sys.stdin = open("input.txt", "r")

def bfs(start):
    queue = deque()
    queue.append(start)
    visited[start] = True   # 대상 학생 방문처리

    while queue:
        student = queue.popleft()
        for tallerStudent in graph[student]:
            if not visited[tallerStudent]:
                queue.append(tallerStudent)
                visited[tallerStudent] = True

    queue = deque()
    queue.append(start)
    while queue:
        student = queue.popleft()
        for i in range(1, N+1):
            for x in graph[i]:
                if x == student and not visited[i]:
                    queue.append(i)
                    visited[i] = True

    flag = True
    for i in range(1, N+1):
        if visited[i] == False:
            flag = False
    if flag:
        global result
        result += 1
T = int(input())

for t in range(1, T+1):
    N, M = int(input()), int(input())
    graph = [[] for _ in range(N+1)]    # 화살표 방향: 작은애 -> 큰애
    # reverseGraph = [[] for _ in range(N + 1)]
    result = 0
    for i in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        # reverseGraph[b].append(a)
    for i in range(1, N + 1):
        visited = [False] * (N + 1)
        bfs(i)
    print(f"#{t} {result}")