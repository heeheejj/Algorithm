# 간단한 369게임

n = int(input())
 
for i in range(1, n+1):
    cnt = list(str(i)).count("3") + list(str(i)).count("6") + list(str(i)).count("9")
    if cnt > 0:
        print("-"*cnt, end=' ')
    else:
        print(i, end=' ')