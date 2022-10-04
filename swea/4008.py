# 숫자 만들기

import sys

def calculate(op, a, b):
    if op == 0:
        return a + b
    elif op == 1:
        return a - b
    elif op == 2:
        return a * b
    elif op == 3:
        if a * b < 0:
            return -1*(abs(a)//abs(b))
        elif a < 0 and b < 0:   # 둘다 음수인 경우
            return abs(a) // abs(b)
        else:   # 둘 다 양수인 경우
            return a // b
def setOrder():
    resultMax, resultMin = 0, 99999
    for i in range(N-1):
        orderResult = list()
        for j in range(4):
            if opCnt[j] != 0:
                if j == 0:  # +
                    calculate(0, nums[i], nums[i+1])
                elif j == 1:
                    orderResult.append(1)
                elif j == 2:
                    orderResult.append(2)
                elif j == 3:
                    orderResult.append(3)
                opCnt[j] = opCnt[j] - 1
        print(orderResult)

sys.stdin = open("input.txt", "r")
# input = sys.stdin.readline
T = int(input())

for t in range(1, T+1):
    N = int(input())
    opCnt = list(map(int, input().split()))
    nums = list(map(int, input().split()))

    setOrder()
    # for i in range(N-1):
    #     calculate()
    # #print(f"#{t} {result}")