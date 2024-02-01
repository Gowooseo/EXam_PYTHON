#----------------------------------------------------------
# for i in range(7):
#     for j in range(3):
#         print('*',end='')
#     print()

#계단식으로 별 출력하기
# for i in range(5):
#     for j in range(5):
#         if j<=i :        # 0<=0,1개 - 1<=0,1,2개 - 2<=0,1,2, 3개 이런식으로 별이 찍힘
#             print('*',end='')
#     print()

# 대각선으로 별 출력하기
# for i in range(5):
#     for j in range(5):
#         if i==j:
#             print('*',end='')
#         else :
#             print(' ',end='')
#     print()

# 절반 삼각형 출력하기

# for i in range(5):
#     for j in range(5):
#         if j<=i:
#             print('*',end='')
#         else :
#             print(' ',end='')
#     print()

# 19.6 역삼각형 모양 별 출력하기
a = int(input())
for i in range(a):
  for j in range(a-i-1):
    print(' ',end='')
  for j in range(2*i+1):
    print('*',end='')
  print()




# 18.6 심사문제: 두 수 사이의 숫자 중 3으로 끝나지 않는 숫자 출력하기
# 표준 입력으로 정수 두 개가 입력됩니다(첫 번째 입력 값의 범위는 1~200,
# 두 번째 입력 값의 범위는 10~200이며 첫 번째 입력 값은 두 번째 입력 값보다 항상 작습니다).
# 다음 소스 코드를 완성하여 첫 번째 정수와 두 번째 정수 사이의 숫자 중 3으로 끝나지 않는
# 숫자가 출력되게 만드세요.
# 정답에 코드를 작성할 때는 while True:에 맞춰서 들여쓰기를 해주세요.
