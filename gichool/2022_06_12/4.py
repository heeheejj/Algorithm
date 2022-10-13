# 풀다 말음
# dfs 쓰는게 맞나?
def dfs(grid, x, y):
    if x < 0 or x >= n or y < 0 or y >= m:
        return
    if grid[x][y] == "#":
        return
    else:   # 이동 가능
        dfs(x+1, y)
        dfs(x-1, y)
        dfs(x, y+1)
        dfs(x, y-1)

dx = [0, 1 , 0, -1]
dy = [1, 0, -1, 0]
n, m = 0, 0
def solution(grid, k):
    answer = -1
    n = len(grid)
    m = len(grid[0])
    dfs(grid, 0,0)
    return answer