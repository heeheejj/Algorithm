# 모의 SW 역량테스트 - 무선 충전

import sys
input = sys.stdin.readline

T = int(input())

dx = [0, 0, 1, 0, -1]
dy = [0, -1, 0, 1, 0]

def isBCRange(int x, int y):
  

for t in range(1, T+1):
  print("#" + str(t), end=' ')  # TC 갯수
  M, A = map(int, input().split())  # M: 총 이동시간
  aPath = list(input().split())
  bPath = list(input().split())
  
  BC = list()
  BC.append(tuple(map(int, input().split())))

  # A와 B 이동시키기
  ax, ay, bx, by = 1, 1, 10, 10
  for m in range(M+1):
    aDirIdx = aPath[m]
    ax += dx[aDirIdx]
    ay += dy[aDirIdx]

    bDirIdx = bPath[m]
    bx += dx[bDirIdx]
    by += dy[bDirIdx]

    
    