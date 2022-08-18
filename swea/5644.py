# 모의 SW 역량테스트 - 무선 충전

import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

T = int(input())

dx = [0, 0, 1, 0, -1]
dy = [0, -1, 0, 1, 0]

def getChargableAmount(x, y):
  chargeAmount = [0 for _ in range(A)]  # (x, y)위치가 i번째 BC의 충전범위면 그 충전량을 저장하는 배열
  
  for i in range(A):
    bcX, bcY = BC[i][0], BC[i][1]  # i번째 BC의 x좌표, y좌표
    if abs(x - bcX)+abs(y-bcY) <= BC[i][2]:  # temp[2] = i번째 BC의 C (충전 범위)
      chargeAmount[i] = BC[i][3]
  return chargeAmount
      
def getMaxAmount(a, b):  # a, b 사용자가 각각 (x, y)좌표에 있을 때 몇번째 BC범위 안에 있는지 저장하는 리스트를 파라미터로 넘겨줌
  maxAmount = 0  # 특정 좌표(x, y)에서의 최대 충전량
  if A == 1: # BC가 하나일 때 다른 BC와 비교해줄 필요 없음
    return max(a[0], b[0])

  # A사용자가 i번쨰 BC, B사용자가 j번쨰 BC 쓸 때
  for i in range(A):
    for j in range(A):
      if i != j:
        maxAmount = max(a[i]+b[j], maxAmount)  #뭐야 이게
  return maxAmount
  
for t in range(1, T+1):
  result = 0
  print("#" + str(t), end=' ')  # TC 갯수
  M, A = map(int, input().split())  # M: 총 이동시간
  aPath = list(map(int, input().split()))
  bPath = list(map(int, input().split()))

  BC = [list(map(int, input().split())) for _ in range(A)]

  # A와 B 이동시키기
  ax, ay, bx, by = 1, 1, 10, 10

  # (1, 1), (10, 10)일 때는 for문 안에 포함 안돼서 여기서 더해줌
  a_chargeAmount = getChargableAmount(ax, ay)
  b_chargeAmount = getChargableAmount(bx, by)
  result += getMaxAmount(a_chargeAmount, b_chargeAmount)
  for m in range(M):
    aDirIdx = aPath[m]
    ax += dx[aDirIdx]
    ay += dy[aDirIdx]
    a_chargeAmount = getChargableAmount(ax, ay)
    
    bDirIdx = bPath[m]
    bx += dx[bDirIdx]
    by += dy[bDirIdx]
    b_chargeAmount = getChargableAmount(bx, by)

    result += getMaxAmount(a_chargeAmount, b_chargeAmount)

  print(result)