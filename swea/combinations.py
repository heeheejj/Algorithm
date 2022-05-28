# deque 이용
from collections import deque

def dfs(deq, depth):
    if len(deq) == M:  # 종료 조건 1 : M개를 모두 선택했을 때
        print(deq)  # 선택 후의 알고리즘 호출
        return
    elif depth == len(some_list):  # 종료 조건 2: 리스트의 마지막 까지 탐색했을 때
        return
 
    # 현재 depth의 값 포함 재귀 호출
    deq.append(some_list[depth])
    dfs(deq, depth + 1)
 
    # 현재 depth의 값 미포함 재귀 호출
    deq.pop()
    dfs(deq, depth + 1)

k = 3
dfs(deq, k)