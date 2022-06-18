# 이미 정렬되어있으므로 이분탐색 써야 시간초과 안난다고 함 -> 수정 필요

def solution(n, plans, clients):
    answer = [0]*len(clients)
    
    for i in range(len(clients)):
        bss = list()
        c_bss = list()
        c_list = list()
        c_list = clients[i].split()
        for c_bs in c_list[1:]:
            c_bss.append(c_bs)
        for j in range(len(plans)):
            
            p_list = list()
            p_list = plans[j].split()
            if int(p_list[0]) < int(c_list[0]):
                for added_bss in p_list[1:]:
                    bss.append(added_bss)
                continue
            else:
                for added_bss in p_list[1:]:
                        bss.append(added_bss)
                if set(bss).intersection(set(c_bss)) == set(c_bss):
                    answer[i] = j+1
                    break
    return answer