#--------------------------------------------------------
# [실습1] 아래 데이터에 있는 점수를 화면에 한줄에 한개씩 출력
#        단, 점수가 70점 이상인 것만 출력
#--------------------------------------------------------
jumsus=[98, 45, 72, 45, 98, 70, 34, 99, 100]
for i in jumsus:
    if int(i)>=70:
        print(i,end=' ')
print()
idx=0
count=len(jumsus)
while idx<count:
    if jumsus[idx]>=70:
        print(jumsus[idx],end=' ')
    idx+=1
print()

#--------------------------------------------------------
# [실습2] 아래 데이터에 있는 점수를 화면에 한줄에 한개씩 출력
#        단, 점수가 70점 이하인 경우 출력을 정지
#--------------------------------------------------------
jumsus=[98, 85, 72, 45, 68, 70, 34, 99, 100]

for i in jumsus:
    if i<=70:
        break
    print(i,end=' ')
print()


idx=0
count=len(jumsus)
while idx<count:
    if jumsus[idx]<=70:
        break
    print(jumsus[idx],end=' ')
    idx+=1
print()

