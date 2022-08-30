# permutation 구현
def permutation(cnt, nums):
  if cnt == 3:  # 3자리에 뽑을 개수를 넣으면 됨
    print(nums)
    return

  for i in range(n):
    if not visited[i]:
      nums[cnt] = inputs[i]
      visited[i] = True
      permutation(cnt+1, nums)
      visited[i] = False

inputs = [1, 2, 3]
n = len(inputs)
visited = [False]*n
nums = [0]*3  # 3자리에 뽑을 개수를 넣으면 됨
permutation(0, nums)