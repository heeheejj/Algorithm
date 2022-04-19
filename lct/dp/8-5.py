# 효율적인 화폐 구성

import sys
input = sys.stdin.readline
n, m = map(int, input().split())
hp = list()
d = [10001] * (m + 1)
d[0] = 0
for _ in range(n):
  hp.append(int(input().rstrip()))

for i in range(n):  # n종류의 화폐.. 화폐단위 인덱스
  for j in range(hp[i], m + 1):  # 화폐 합 j
    if d[j-hp[i]] != 10001:
      d[j] = min(d[j-hp[i]] + 1, d[j])
  
if d[m] != 10001:    
  print(d[m])
else:
  print("-1")