# SWEA 15172. 헌터
# 순열 직접 구현 - 1815ms
'''
몬스터가 3마리면 1, -1, 2, -2, 3, -3 6개를 나열하는 순열을 구해야한다.
단, -1이 1보다 앞에 오면 안된다.
음수를 그냥 *-1해서 1, 1, 2, 2, 3, 3을 나열하는 순열을 구하고,
isVisitedMonster이라는 boolean배열로 해당 인덱스몬스터가 방문한 몬스터인지 체크해주어
isVisitedMonster가 false이면 monster좌표배열에서 해당 몬스터의 좌표를 꺼내고,
true이면 customer좌표배열에서 해당 몬스터의 좌표를 꺼내는 식으로 했다.

많이 헤맸지만 기억나는것만 정리
isVisitedMonster의 초기화 위치를 잘못해서 헤맸다.
for permOutput in permOutputs: 여기 밖에서가 아니라 안에서,
즉 만들어진 순열 하나를 확인할때마다 초기화를 해주어야한다.
'''
import sys

def getDistance(prevPos, pos):
  x1, y1 = prevPos
  x2, y2 = pos
  return abs(x2-x1)+abs(y2-y1)

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

T = int(input())
for t in range(1, T+1):
  N = int(input())
  inputs = [list(map(int, input().split())) for _ in range(N)]
  monsterPos = [0]*5
  customerPos = [0]*5
  permInputs = list()
  M = 0
  for i in range(N):
    for j in range(N):
      value = inputs[i][j]
      if value == 0:
        continue
      elif value > 0:
        monsterPos[value] = (i, j)
        permInputs.append(value)
        permInputs.append(value)
        M += 1
      else:
        customerPos[-1*value] = (i, j)

  permInputs.sort()
  # permOutputs = list(set(permutations(permInputs, M*2)))
  n = 2*M
  nums = [0]*n
  visited = [False]*n

  permOutputs = list()
  def permutation(cnt, numbers):
    if cnt == n:  # 3자리에 뽑을 개수를 넣으면 됨
      permOutputs.append(tuple(numbers))
      return
    for i in range(n):
      if not visited[i]:
        numbers[cnt] = permInputs[i]
        visited[i] = True
        permutation(cnt + 1, numbers)
        visited[i] = False

  permutation(0, nums)
  permOutputs = list(set(permOutputs))
  minDist = sys.maxsize
  for permOutput in permOutputs:
    dist = 0
    prevPos = (0, 0)
    isVisitedMonster = [False] * (M + 1)  # 고객까지 방문했는지 여부
    for x in permOutput:
      if not isVisitedMonster[x]:
        isVisitedMonster[x] = True
        tempPos = monsterPos[x]
      else:
        tempPos = customerPos[x]
      dist += getDistance(prevPos, tempPos)
      prevPos = tempPos
    minDist = min(minDist, dist)

  print("#"+str(t), minDist)