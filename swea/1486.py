# 장훈이의 높은 선반
# 부분집합 이용

import sys
sys.stdin = open("input.txt", "r")

T = int(input())
def subset(idx, sum):
    global result
    if idx == size: # 모든 경우의 수가 나오면 합이 B 이상인지 확인한다.
        if B <= sum:    # B 이상이면서 result보다 작으면 result의 값 갱신
            result = min(result, sum)
        return  # 더 이상 더해봤자 result값이 갱신될 일이 없으므로 끝낸다.
    if B <= sum:    # 모든 경우의 수가 다 나오지 않았더라도, B 이상이면서 result보다 작으면 result의 값 갱신
        result = min(result, sum)
        return  # 더 이상 더해봤자 result값이 갱신될 일이 없으므로 끝낸다.
    else:
        subset(idx+1, sum + heights[idx])
        subset(idx+1, sum)

for t in range(1, T+1):
    N, B = map(int, input().split())
    heights = list(map(int, input().split()))
    result = float('inf')
    size = len(heights)
    subset(0, 0)
    print(f"#{t} {result-B}")