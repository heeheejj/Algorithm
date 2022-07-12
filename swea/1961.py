# 숫자 배열 회전

import sys
sys.stdin = open("input.txt", "r")
T = int(input())

for t in range(1, T+1):
  print("#"+str(t))
  N = int(input())
  arr = [list(map(int, input().split())) for _ in range(N)]

  