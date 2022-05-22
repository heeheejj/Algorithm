# 미로 탈출
from collections import deque

def bfs(x, y):
  queue = deque()
  queue.append((x, y))
  while queue:
    x, y = queue.popleft()

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if nx < 0 or nx >= n or ny < 0 or ny >= m:
        continue
      if graph[nx][ny] == 0:
        continue
      if graph[nx][ny] == 1:
        queue.append((nx, ny))
        graph[nx][ny] = graph[x][y] + 1 # graph는 원소가 0, 1뿐인 2차원 배열이지만 이렇게 1씩 더해주어 다시 저장해 1, 2, 3, ... 이런식으로 경로가 찍히도록 최단거리의 길이 찾기
    
  return graph[n-1][m-1]

n, m = map(int,input().split())

graph = []
for i in range(n):
    graph.append(list(map(int,input())))

# dx - dy 순서대로 
# 상: (-1,0), 하: (1, 0), 좌: (0, -1), 우: (0, 1)
  
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
#print(graph)

# bfs 호출!
# visited 배열 따로 만들 필요 없이, 1을 0으로 바꿔주면 될 것 같다.
print(bfs(0,0))