# 미생물 격리
# 주석 있는 ver
import sys
dx = [0, -1, 1, 0, 0]
dy = [0, 0, 0, -1, 1]
UP, DOWN, LEFT, RIGHT = 1, 2, 3, 4
def reverseDir(direc):
    if direc == UP:
        direc = DOWN
    elif direc == DOWN:
        direc = UP
    elif direc == LEFT:
        direc = RIGHT
    elif direc == RIGHT:
        direc = LEFT
    return direc

sys.stdin = open("../SWEA/input.txt", "r")

T = int(input())

for t in range(1, T+1):
    N, M, K = map(int, input().split())
    group = [list(map(int, input().split())) for _ in range(K)]  # 미생물 군집 리스트

    # k번째 군집의 (x, y) 위치를 정수 하나(num)으로 표현해서 group[k]의 4번째 원소로 추가
    for k in range(K):  # num 추가
        x = group[k][0]  # x좌표
        y = group[k][1]  # y좌표
        group[k].append(x*N+y)

    for m in range(M):
        # print(f"========================== m: {m} ==============================")
        k = 0
        # print(f"이동 전: {group}")
        while k < K:
            x = group[k][0]  # x좌표
            y = group[k][1]  # y좌표
            nx = x + dx[group[k][3]]
            ny = y + dy[group[k][3]]

            # group에 이동된 위치 일단 반영하기
            group[k][0] = nx
            group[k][1] = ny
            group[k][4] = nx * N + ny

            # 경계에 닿았으면 미생물 반감+방향전환
            if nx == 0 or ny == 0 or nx == N - 1 or ny == N - 1:
                if group[k][2] == 1:
                    group.pop(k)
                    # for i in range(4, -1, -1):
                    #     del group[k][i] # 2차원리스트에서 2차원리스트 안의 1차원리스트를 전부 삭제하려면 하나하나 다 해줘야함
                    # del group[k]
                    k -= 1
                    K -= 1
                else:
                    group[k][2] //= 2
                    group[k][3] = reverseDir(group[k][3])
            k += 1

        # 모든 군집 이동 완료 #
        # print(f"정렬 전: {group}")
        group.sort(key=lambda p:(p[4], -p[2]))  # num기준 오름차순 정렬, num 같을 시 미생물 수 기준 내림차순 정렬

        # print(f"충돌 전: {group}")
        i = 0
        while i < len(group)-1:
            now = group[i][4]  # 현재 군집의 위치idx
            next = group[i + 1][4]  # 다음 군집의 위치idx
            if now == next:
                group[i][2] += group[i+1][2] # 미생물 수 합치기
                group.pop(i+1)
                K -= 1
                i -= 1
            i += 1
        # print(f"충돌 고려 후: {group}")

    result = 0
    # print(f"result group: {group}")
    for j in range(len(group)):
        result += group[j][2]
    print(f"#{t} {result}")