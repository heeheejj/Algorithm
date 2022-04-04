# 소수
import math

def isPrimeNumber(x):
  if x == 1 or x == 0:
    return False
  
  for i in range(2, math.sqrt(x) + 1):  # x == 2이면 for문 안돌고 바로 return True
    if x % i == 0:
      return False
  return True
  
m = int(input())
n = int(input())
sum = 0
min = 0

for i in range(n, m-1, -1):
  if isPrimeNumber(i):  # 만약 소수이면
    sum += i
    min = i

if sum == 0:
  print(-1)
else:
  print(sum)
  print(min)