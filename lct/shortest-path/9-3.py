# 전보

import sys
import heapq

def dijkstra(start):
  q = []
  distance[start] = 0
  heapq.heappush(q, (0, start))  # (거리, 노드)
  
  while q:
    dist, now = heapq.heappop(q)
    if distance[now] < dist:
      continue  
    for i in graph[now]:
      cost = i[1] + dist
      if cost < distance[i[0]]:
        distance[i[0]] = cost
        heapq.heappush(q, (cost, i[0]))

INF = int(1e9)

input = sys.stdin.readline

n, m, c = map(int, input().split())

graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)

for _ in range(m):
  x, y, z = map(int, input().split())
  graph[x].append((y, z))

dijkstra(c)

cnt = 0
max_time = 0
for d in distance:
  if d != INF:
    cnt += 1
    max_time = max(max_time, d)

print(cnt - 1, max_time)