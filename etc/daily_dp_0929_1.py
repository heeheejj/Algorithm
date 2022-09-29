import sys

input = sys.stdin.readline
# 주의: 노란색 페인트 세번 이상 연속도 가능!
dp = [0]*9
dp[1], dp[2] = 2, 3
for i in range(3, 9):
    dp[i] = dp[i-2]+dp[i-1]
print(dp[8])