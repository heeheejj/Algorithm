# 햄버거 다이어트
# 파워셋
def check(idx, score, cal):
    global score_max
     
    if cal > l:
        return
     
    if score > score_max:
        score_max = score
     
    if idx == n:
        return
     
    check(idx+1, score, cal)
    check(idx+1, score + inputs[idx][0], cal + inputs[idx][1])
 
t = int(input())
 
for i in range(1, t+1):
    print("#" + str(i), end=' ')  # TC 갯수
 
    n, l = map(int, input().split())    # 재료의 수, 제한 칼로리
    inputs = list()
    for _ in range(n):
        t, k = map(int, input().split())
        inputs.append((t, k))
     
    score_max = 0
    check(0, 0, 0)
    print(score_max)