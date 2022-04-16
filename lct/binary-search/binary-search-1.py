# 이진 탐색 (재귀함수로 구현)
# 이미 정렬된 데이터일 때를 전제조건으로 함
# 반으로 쪼개면서 탐색
# 시간복잡도 O(log N)
# 참고: log 밑 2 생략

def binary_search(array, target, start, end):
  if start > end:
    return None

  mid = (start + end) // 2

  if target == array[mid]:
    return mid
  elif target < array[mid]:
    return binary_search(array, target, start, mid - 1)
  else:
    return binary_search(array, target, mid + 1, end)
    
n, target = list(map(int, input().split()))
array = list(map(int, input().split()))

result = binary_search(array, target, 0, n-1)

if result != None:
  print(result + 1)
else:
  print("원소가 존재하지 않습니다.")