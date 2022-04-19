# 개미 전사

n = int(input())
k = list(map(int, input().split()))

result = [0] * n

result[0], result[1] = k[0], max(k[0], k[1])
for i in range(2, n):
  result[i] = max(result[i - 2] + k[i], result[i - 1])

print(result[n-1])