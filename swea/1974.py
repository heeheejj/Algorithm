# 스도쿠 검증

# import sys

# sys.stdin = open("input.txt", "r")
T = int(input())

def check(mat):
  for i in range(9):
    row_check = [0] * 10
    col_check = [0] * 10
    for j in range(9):
      # 가로 확인
      row = mat[i][j]
      if row_check[row]:
        return 0

      # 세로 확인
      col = mat[j][i]
      if col_check[col]:
        return 0

      row_check[row] = 1
      col_check[col] = 1

      if i % 3 == 0 and j % 3 == 0:
        block = [0] * 10
        for k in range(i, i+3):
          for l in range(j, j+3):
            num = mat[k][l]
            if block[num]:
              return 0
            block[num] = 1
  return 1

for t in range(1, T+1):
  print("#"+str(t), end=' ')
  arr = [list(map(int, input().split())) for _ in range(9)]
  result = check(arr)
  print(result)