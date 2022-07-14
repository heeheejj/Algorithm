# 숫자 배열 회전

# import sys

# sys.stdin = open("input.txt", "r")
T = int(input())

def rotate(a, N):  # 2차원배열을 90도 돌리는 함수
  _a = [[0] * N for _ in range(N)]
  for i in range(N):
    for j in range(N):
      _a[i][j] = a[N-j-1][i]
  return _a

for t in range(1, T+1):
  print("#"+str(t))
  N = int(input())
  arr = [list(input().split()) for _ in range(N)]
  result1 = rotate(arr, N)
  result2 = rotate(result1, N)
  result3 = rotate(result2, N)
  for i in range(N):
    print("".join(result1[i]), end=' ')
    print("".join(result2[i]), end=' ')
    print("".join(result3[i]), end=' ')
    print()