# SWEA15160. 낚시터 자리잡기

import sys
from itertools import permutations
def left(gatePos, dist): # 왼쪽방향으로 자리잡는 함수, dist는 gate로부터 떨어진 거리를 말한다.
  global grid, cnt
  if gatePos - dist >= 0 and grid[gatePos-dist] == 0: # 자리잡을 위치가 범위 내고, 자리잡을 위치에 아무도 자리잡지 않았다면
    grid[gatePos-dist] = dist+1 # dist + (게이트에서 위 방향으로 이동하는 거리 1) 해주고 저장
    cnt += 1  # 낚시터에 입장한 사람 수

def right(gatePos, dist): # 오른쪽방향으로 자리잡는 함수, dist는 gate로부터 떨어진 거리를 말한다.
  global grid, cnt
  if gatePos + dist < N and grid[gatePos+dist] == 0: # 자리잡을 위치가 범위 내고, 자리잡을 위치에 아무도 자리잡지 않았다면
    grid[gatePos+dist] = dist+1 # dist + (게이트에서 위 방향으로 이동하는 거리 1) 해주고 저장
    cnt += 1  # 게이트 당 낚시터에 입장한 사람 수

sys.stdin = open("input.txt", "r")
T = int(input())

for t in range(1, T+1):
  N = int(input())
  gates = [tuple(map(int, input().split())) for _ in range(3)]
  gateOrderPermInputs = [0, 1, 2]
  gateOrderPermOutputs = list()
  isVisited = [False]*3
  nums = [0]*3

  gateOrderPermOutputs = list(permutations(gateOrderPermInputs, 3))
  ways = [[left, right], [right, left]] # 어느 방향으로
  minDist = float('inf')
  for order in gateOrderPermOutputs:

    for way in ways:  # 2번 반복하는데, 첫번째는 왼쪽을 우선으로 자리잡고 두번째는 오른쪽을 우선으로 자리잡음
      def1, def2 = way
      grid = [0] * N
      for x in order:
        cnt = 0  # 입장한 사람 수
        gatePos = gates[x][0] - 1
        waitingCnt = gates[x][1]
        dist = 1
        if grid[gatePos] == 0:
          grid[gatePos] = dist
          cnt += 1

        while cnt < waitingCnt:
          def1(gatePos, dist) #한 쪽 방향으로 자리잡기
          if cnt == waitingCnt: break
          def2(gatePos, dist) #반대쪽 방향으로 자리잡기
          dist += 1
      distByOrder = sum(grid)
      minDist = min(minDist, distByOrder)
  print(f"#{t} {minDist}")