# 떡볶이 떡 만들기

import sys

input = sys.stdin.readline

n, m = map(int, input().split())
ddeok = list(map(int, input().split()))

start = 0
end = max(ddeok)

result = 0
while start <= end:
    mid = (start + end) // 2
    sum = 0
    for x in ddeok:
      if x > mid:
        sum += x - mid
    if sum >= m:
      start = mid + 1
      result = mid
    else:
      end = mid - 1

print(result)