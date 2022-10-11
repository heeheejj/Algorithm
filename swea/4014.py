# 활주로 건설

import sys

sys.stdin = open("input.txt", "r")
def makeRoad(line): # 하나의 행 or 열을 검사, 활주로 건설 가능하면 true, 불가능하면 false return
    same = 0
    j = 0
    while j < N-1:
        if j == 0:
            same = 1
        diff = line[j] - line[j + 1]
        if diff == 0:
            same += 1
        elif diff == -1:  # 올라갈 경우
            if same < X:
                return False  # 같은높이가 연속으로 나타난 횟수가 X보다 작으면 활주로 건설 불가
            else:
                same = 1  # 같은높이가 연속으로 나타난 횟수가 X이상이면 활주로 건설 가능, same을 1로 초기화
        elif diff == 1: # 1만큼 내려가는 경우
            sameNext = 1
            j += 1
            point = j
            for k in range(point, point+X-1): #활주로 길이만큼 공간이 있는지 판단
                if k+1 >= N:  #범위를 넘어가는 경우 활주로 건설 불가
                    return False
                if line[k] == line[k+1]:
                    sameNext += 1
            if sameNext < X:
                return False
            else:
                j += (X-1)
                same = 0
                # same을 1로 해주면 경사로 길이 2일 때 2 1 1 1 2 2 같은 경우
                # 2인덱스의 1까지 경사로를 놓고나서 2로 다시 올라갈 때 same이 1이어야하는데 2가되므로 건설 불가능이 건설가능으로 처리된다..
                # 애초에 맨처음부터 same = 0으로 놓고, 첫 인덱스라면 same=1으로 바꾸는 방식을 썼다.
                continue
        else:  # 높이차이가 2 이상인 경우 활주로 건설 불가, same 1로 초기화
            return False
        j += 1
    return True

T = int(input())

for t in range(1, T+1):
    N, X = map(int, input().split())
    _map = [list(map(int, input().split())) for _ in range(N)]

    _map2 = list()  # _map 2차원배열의 전치행렬
    for i in range(N):
        line = list()
        for j in range(N):
            line.append(_map[j][i])
        _map2.append(line)

    result = 0
    for i in range(N):
        if makeRoad(_map[i]):
            result += 1
        if makeRoad(_map2[i]):
            result += 1

    print(f"#{t} {result}")