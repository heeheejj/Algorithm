n = int(input())
a = list(map(int, input().split()))
a.sort()
count = 0
result = 0
for i in range(n):
  count += 1
  if count >= a[i]:
    result += 1
    count = 0
print(result)

# f-string 포메팅으로 변수를 문자열에 바로 대입
a = 1
b = 2

print(f"{a} + {b} 는 몇일까? " )

# 012302 문자 하나하나 숫자로 mapping해서 리스트 담기
# ex) input이 010231일 때 a = [0, 1, 0, 2, 3, 1]
a = list(map(int,input()))  