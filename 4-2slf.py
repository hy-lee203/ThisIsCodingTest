# 00시 00분 00초에서 n시 59분 59초 까지 3이 하나라도 포함된 시간은 몇개인가?
# 23시 59분 59초까지 있음

n=int(input())
count=0

# 전체-3이 없는 시간
total=23*59*59

#초기화
cnt_o=0
cnt_t=0

#시간에서 3없는 개수
for i in range (1, 24):
    if i%10==3:
        cnt_o+=1
    if i//10==3:
        cnt_t+=1
ncnt_h=23-cnt_o*cnt_t

#초기화
cnt_o=0
cnt_t=0

#분, 초 에서 3없는 개수
for i in range (1, 60):
    if i%10==3:
        cnt_o+=1
    if i//10==3:
        cnt_t+=1
ncnt_h=60-cnt_o*cnt_t


"""
2개
10+5
15개
15개

총 (n+1)*60*60개

n이 3보다 작으면 
전체-(n+1)*45*45

크면
전체-n*45*45

5
6*60*60-5*45*45
21600 10125
"""