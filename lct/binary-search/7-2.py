# 부품 찾기

import sys

def binary_search(array, target, start, end):
  if start > end:
    return False

  mid = (start + end) // 2

  if target == array[mid]:
    return True
  elif target < array[mid]:
    return binary_search(array, target, start, mid - 1)
  else:
    return binary_search(array, target, mid + 1, end)

input = sys.stdin.readline

n = int(input())
dongbin = list(map(int, input().split()))
dongbin.sort()

m = int(input())
sonnim = list(map(int, input().split()))

for x in sonnim:
  if binary_search(dongbin, x, 0, n - 1):
    print("yes", end = ' ')
  else:
    print("no", end = ' ')