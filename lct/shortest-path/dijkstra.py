# 힙을 이용한 다익스트라 알고리즘 - 혼자서 해보기 ~! 성공!~!~
# 한 지점에서 다른 특정 지점까지의 최단 경로를 구해야 하는 경우
# 시간복잡도: O(ElogV) / E: 최대 간선의 개수, V: 노드의 개수 / 설명은 p.250 참고

import heapq
import sys

input = sys.stdin.readline

INF = int(1e9)

# 노드 개수, 간선 개수 입력받기 n, m
n, m = map(int, input().split())
# 시작 노드 번호 입력받기 
start = int(input())

# 노드, 간선 정보 담는 테이블 초기화
graph = [[] for i in range(n+1)]
# 최소 비용 테이블 초기화
distance = [INF] * (n + 1)

# 모든 간선 정보 입력받기 (a b c) -> a번노드에서 b번노드로 가는 비용이 c
for _ in range(m):
  a, b, c = map(int, input().split())
  graph[a].append((b, c))

def dijkstra(start):

  q = []

  heapq.heappush(q, (start, 0))
  distance[start] = 0

  while q:  # 큐가 빌 때 까지
    now, dist = heapq.heappop(q)
    if distance[now] < dist:
      continue
    for i in graph[now]:
      cost = dist + i[1]
      if cost < distance[i[0]]:
        distance[i[0]] = cost
        heapq.heappush(q, (i[0], cost))

dijkstra(start)

for i in range(1, n+1):
  if distance[i] != INF:
    print(distance[i])
  else:
    print("INFINITY")