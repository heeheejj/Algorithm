import sys
sys.stdin = open("input2.txt", "r")
dx = [1, 0 , -1, 0]
dy = [0, 1, 0, -1]
minDirIdx = -1

def updateMatrix(tempMatrix, updateX, updateY):
    tempMatrix[updateX][updateY] = True
    nx = updateX+dx[minDirIdx]
    ny = updateY+dy[minDirIdx]
    while 0 <= nx < N and 0 <= ny < N:
        tempMatrix[nx][ny] = True
        nx += dx[minDirIdx]
        ny += dy[minDirIdx]


def updateMinVal(t_tempCores, tempMatrix, coreInfoIdx, cores):
    tempCores = cores[:]

    global minDirIdx
    minDirIdx  # 최솟값나올때의 방향 idx 기억!!

    coreInfo = tempCores[coreInfoIdx]
    print("coreInfo:", coreInfo)
    minVal, x, y = coreInfo[0], coreInfo[1], coreInfo[2]
    isConnected = False
    minDist = 9999
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        dist = 999
        print("nx:", nx,"ny:",ny, "N:",N)
        while 0 <= nx < N and 0 <= ny < N:  # 가장자리까지 연결완료될때까지 반복
            if tempMatrix[nx][ny]:
                print("break")
                break
            else:
                nx += dx[i]
                ny += dy[i]
                print("nx:",nx,"ny:",ny)
                if nx == N:
                    dist = N - x - 1
                    if dist < minDist:
                        minDist = dist
                        minDirIdx = 0
                elif ny == N:
                    dist = N - y - 1
                    if dist < minDist:
                        minDist = dist
                        minDirIdx = 1
                elif nx == 0:
                    dist = x
                    if dist < minDist:
                        minDist = dist
                        minDirIdx = 2
                elif ny == 0:
                    dist = y
                    if dist < minDist:
                        minDist = dist
                        minDirIdx = 3
    print("x:",x,"/ y:",y,"/ minDist:",minDist)
    if not minDist == 9999:
        tempCores[coreInfoIdx] = (minDist, x, y)
        t_tempCores[coreInfoIdx] = (minDist, x, y)
        return tempCores
    else:
        return -1


def subset(arr, visited, cnt):
    if cnt == coreCnt:
        nums = list()
        for i in range(coreCnt):
            if visited[i]:
                # nums.append(arr[i])
                nums.append(i)
        sum = 0
        tempMatrix = matrix[:]
        tempCores = cores[:]
        t_tempCores = tempCores
        updatedCores = tempCores[:]
        global minDirIdx
        minDirIdx = -1
        print("nums:",nums)
        for idx in nums:
            x = arr[idx]
            print(tempCores[x], end=' ')
            updatedCores = updateMinVal(t_tempCores, tempMatrix, x, tempCores)
            if updatedCores == -1:
                return

            updatedCores.sort()
            print("updatedCores: ", updatedCores)
            sum += updatedCores[0][0]
            updateMatrix(tempMatrix, updatedCores[0][1], updatedCores[0][2]) # 해당 core 좌표와 전선 1로 바꾸기

            updatedCores.remove(t_tempCores[x])
        print()
        global result
        if sum < result:
            result = sum
        return

    visited[cnt] = True
    subset(arr, visited, cnt+1)

    visited[cnt] = False
    subset(arr, visited, cnt+1)

T = int(input())
for t in range(1, T+1):
    N = int(input())
    matrix = [[False]*N for _ in range(N)]
    cores = list()  # 각 코어당 (상하좌우중 최솟값, x좌표, y좌표) 를 저장
    for i in range(N):
        line = list(map(int, input().split()))
        for j in range(N):
            token = line[j]
            if token == 1:
                matrix[i][j] = True
                if i == 0 or j == 0 or i == N-1 or j == N-1:
                    continue
                cores.append((999, i, j))
    coreCnt = len(cores)
    print(coreCnt)
    subsetInputs = [i for i in range(coreCnt)]
    coreCnt = len(subsetInputs)
    visited = [False] * coreCnt
    result = 99999
    subset(subsetInputs, visited, 0)
    print(result)