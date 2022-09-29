import sys

input = sys.stdin.readline

dp = [0]*9
dp[1], dp[2] = 2, 3
for i in range(3, 9):
    dp[i] = dp[i-2]+dp[i-1]
print(dp[8])