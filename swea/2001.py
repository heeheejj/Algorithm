# 파리 퇴치

t = int(input())
for i in range(1, t+1):
    print("#" + str(i), end=' ')  # TC 갯수
 
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    max_sum = 0
    for i in range(n-m+1):
        for j in range(n-m+1):
            sum = 0
            for nx in range(m):
                for ny in range(m):
                    sum += arr[i+nx][j+ny]
            max_sum = max(max_sum, sum)
    print(max_sum)