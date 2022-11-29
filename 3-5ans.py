# n, k를 공백으로 입력받기
n,k=map(int, input().split())
result=0

while True:
  # n==k로 나누어 떨어지는 수가 될 때까지 1빼기
  target=(n//k)*k
  result+=(n-target)
  n=target
  # n이 k 보다 작을 떄 반복문 탈출
  if n<k:
    break
  # k로 나누기
  result+=1
  n//=k

# 마지막으로 남은 수에 대하여 1씩 빼기
result+=(n-1)
print(result)
