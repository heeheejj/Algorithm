# 중간 평균값 구하기

t = int(input())
 
for i in range(1, t+1):
    print("#"+str(i), end=' ')
    tc = list(map(int, input().split()))
    tc.sort()
    tc.pop(0)
    tc.pop(len(tc)-1)
    print(int(sum(tc)/len(tc)+0.5))