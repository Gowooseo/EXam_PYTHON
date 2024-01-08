# i=0
# while True:
#     print(i)
#     i+=1
#     if i==100:
#         break
#
#
# for z in range(10000):
#     if z%2==1:
#         print(z)
#
# # 입력한 횟수대로 반복하기
#
# count=int(input('반복 횟수 입력:'))
# t=0
# while True:
#     print(t)
#     t+=1
#     if t==count:
#         break
#
#
# #연습문제: 3으로 끝나는 숫자만 출력
# i1=0
# while True:
#     if i1%10!=3:
#         i1+=1
#         continue
#     if i1>73:
#         break
#     print(i1,end=' ')
#     i1+=1

# 18.6 두 수 사이의 숫자 중 3으로 끝나지 않는 숫자 출력
# start,stop=map(int,input().split())
#
# for i in range(start,stop+1):
#     if i%10==3:




for num in range(10):
    for dan in range(2,10):
        if num :
            print(f'{dan}*{num}={dan*num}',end=" " if dan!=9 else '\n')
        else:
            print(f'---{dan}단---',end='  ',)
    print()