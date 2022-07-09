# 두 개의 숫자열
import sys
sys.stdin = open("input.txt", "r")
T = int(input())

for t in range(1, T+1):
  n, m = map(int, input().split())
  a = list(map(int, input().split()))
  b = list(map(int, input().split()))
  
  if n > m:  # 크기가 작은 리스트가 a가 되도록 한다.
    a, b = b, a
    n, m = m, n

  maxSum = 0
  for i in range(m-n+1):
    sum = 0
    for j in range(n):
      sum += a[j] * b[j+i]
      # print(t, "t", j, i)
    maxSum = max(maxSum, sum)

  print("#"+str(t), end=' ')
  print(maxSum)

