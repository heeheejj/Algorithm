def isVIP(gigan, yearpay):
    if yearpay >= 600000:
        if gigan >= 60:
            return True
        if yearpay >= 900000 and gigan >= 24:
            return True
        return False
    return False

def solution(periods, payments, estimates):
    unVIPCnt, newVIPCnt = 0, 0
    n = len(periods)
    vips = [False] * n
    for i in range(n):
        # 이번달의 vip와 unvip를 판단
        if isVIP(periods[i],sum(payments[i])):
            vips[i] = True
        # 다음달의 vip여부 변화를 판단 + 처리
        if isVIP(periods[i]+1, sum(payments[i][1:])+estimates[i]):
            if vips[i] == False:    # unvip에서 vip
                newVIPCnt += 1
        else:
            if vips[i] == True: # vip에서 unvip
                unVIPCnt += 1
    return [newVIPCnt, unVIPCnt]