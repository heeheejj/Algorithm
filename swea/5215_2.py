def dfs(level, beginWith):
    if level == r: # r개를 뽑은 경우
        # print(result)
        return True
    global score_sum
    global cal_sum
    for i in range(beginWith, len(inputs)):
        score_sum += inputs[i][0]
        cal_sum += inputs[i][1]
        if cal_sum > l:
            return False
        # result[level] = inputs[i]
        dfs(level+1, i+1)

# def check(idx, score, cal):
#     global score_max
#
#     if cal > l:
#         return
#
#     if score > score_max:
#         score_max = score
#
#     if idx == n:
#         return
#
#     check(idx+1, score, cal)
#     check(idx+1, score + inputs[idx][0], cal + inputs[idx][1])

t = int(input())

for i in range(1, t+1):
    print("#" + str(i), end=' ')  # TC 갯수

    n, l = map(int, input().split())    # 재료의 수, 제한 칼로리
    inputs = list()
    for _ in range(n):
        t, k = map(int, input().split())
        inputs.append((t, k))

    score_max = 0
    for r in range(1, n+1):
        score_sum = 0
        cal_sum = 0
        if dfs(0,0):
            score_max = max(score_max, score_sum)
    print(score_max)



    # for j in range(1, n+1):
        # for combs in combinations(inputs, j):
        #     t_sum = 0
        #     k_sum = 0
        #     for comb in combs:
        #         t_sum += comb[0]
        #         k_sum += comb[1]
        #     if k_sum > l:
        #         continue
        #     else:
        #         t_sum_max = max(t_sum_max, t_sum)
#
#     print(t_sum_max)
#
#
#
#
#
#
#
#
#
#
#
#
#
# t = int(input())
#
# # def combinations(array, r):
# #     for i in range(len(array)):
# #         if r == 1:
# #             yield [array[i]]
# #         else:
# #             for next in combinations(array[i+1:], r-1):
# #                 yield [array[i]] + next
# #
# # def combinations2(lst, k):
# #     if k == 0:
# #         return [[]]
# #     arr = []
# #     for x in range(0, len(lst)):
# #         m = lst[x]
# #         _lst = lst[x+1:]
# #         for p in combinations2(_lst, k-1):
# #             arr.append([m]+p)
# #     return arr
#
# # combinations(k+1, score + scoreLst(k), cal+calLst(k) : 포함
# # combinations(k+1, score, cal) : 비포함
#
# def combination(idx, score, cal):
#     global score_max
#
# for i in range(1, t+1):
#     print("#" + str(i), end=' ')
#
#     n, l = map(int, input().split())
#     ts = list()
#     ks = list()
#
#     for _ in range(n):
#         t, k = map(int, input().split())
#         ts.append(t)
#         ks.append(k)
#
#     # ts_sums = list()
#     score_max = 0
#     for j in range(1, n+1):
#         combs = list(combinations(ks, j))
#         for k in range(len(combs)):
#             combinations(ts, j))[k]
#             ts_sums.append(sum(list(combinations(ts, j))[k]))
#     print(score_max)