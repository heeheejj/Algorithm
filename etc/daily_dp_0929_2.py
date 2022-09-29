import sys

input = sys.stdin.readline

dp = [0]*7
dp[1], dp[2] = 2, 5
for i in range(3, 7):
    # (dp[i-2]에 빨간색 하나 추가하는 경우: dp[i-2]가지)
    # + (dp[i-1]에 노란색 or 파란색 추가하는 경우: dp[i-1]*2가지)
    dp[i] = dp[i-2] + dp[i-1]*2
print(dp[6])