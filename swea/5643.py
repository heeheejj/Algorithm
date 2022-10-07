# [Professional] 키 순서
# 1555 ms
# 53분 걸림
# graph: 화살표 방향이 키 더 작은애 -> 키 더 큰애
# reverseGraph: 키 더 큰애 -> 키 더 작은애
import sys
from collections import deque
sys.stdin = open("input.txt", "r")

def bfs(start):
    global result
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
        for smallerStudent in reverseGraph[student]:
            if not visited[smallerStudent]:
                queue.append(smallerStudent)
                visited[smallerStudent] = True

    flag = True
    for i in range(1, N+1):
        if visited[i] == False:
            flag = False
    if flag:

        result += 1
T = int(input())

for t in range(1, T+1):
    N, M = int(input()), int(input())
    graph = [[] for _ in range(N+1)]    # 화살표 방향: 작은애 -> 큰애
    reverseGraph = [[] for _ in range(N + 1)]
    result = 0
    for i in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        reverseGraph[b].append(a)

    for i in range(1, N+1):
        visited = [False]*(N+1)
        bfs(i)
    print(f"#{t} {result}")