n,k=map(int, input().split())
result=0

while True:
    if n==1:
        break
    elif n%k==0:
        result+=1
        n/=k
    else:
        n-=1
        result+=1

print(result)