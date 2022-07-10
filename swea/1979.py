# 어디에 단어가 들어갈 수 있을까

import sys

sys.stdin = open("input.txt", "r")

T = int(input())

for t in range(1, T+1):
  N, K = map(int, input().split())
  arr = [list(map(int, input().split())) for _ in range(N)]

  result = 0
  for i in range(N):
    len = 0  # 길이를 잰다  

    # 행을 검사
    for j in range(N):
      if arr[i][j] == 1:
        len += 1
      if arr[i][j] == 0 or j == N-1:  # 0을 만남(단어가 끝남 or 시작안함) or 행의 끝
      # elif로하면 열의 마지막이 1인 경우 최종길이를 확인 못함
        if len == K:  # 최종길이가 K일 때
          result += 1
        len = 0

    # 열을 검사
    for j in range(N):
      if arr[j][i] == 1:
        len += 1
      if arr[j][i] == 0 or j == N-1:  # 0을 만남(단어가 끝남 or 시작안함) or 열의 끝
      # elif로하면 열의 마지막이 1인 경우 최종길이를 확인 못함
        if len == K:  # 최종길이가 K일 때
          result += 1
        len = 0
  
  print("#"+str(t), end=' ')
  print(result)