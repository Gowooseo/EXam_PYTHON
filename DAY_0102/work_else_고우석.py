#14.1 else 사용하기
#else는 단독 사용 불가

#번외: if 조건문 다르게 표현하기
x=5
if x==10:
    y=x
else:
    y=0

s=5
y=x if x==10 else 0

# 같은 조건문 즉, 변수= 값 if 조건문 else 값

# 14.2 else와 들여쓰기
#else도 if 문과 마찬가지로 들여쓰기를 해야한다.

# 14.3 if 조건문의 동작 방식 알아보기
if True:
    print('참')
else:
    print('거짓')

if False:
    print('참')
else:
    print('거짓')

if None:
    print('참')
else:
    print('거짓')

# 14.3.1 if 조건문에 숫자 지정
if 0:
    print('참')
else:
    print('거짓')

if 1:
    print('참')
else:
    print('거짓')

if hex(35):
    print('참')
else:
    print('거짓')


# 14.3.2 if 조건문에 문자열 지정하기
if 'Hello':
    print('참')
else:
    print('거짓')
# 'Hello'라는 문자열이 있으므로 참입니다.
if '':
    print('참')
else:
    print('거짓')
# ''으로 공백이므로 자연스럽게 False가 됩니다.

# 14.4 조건식 여러개 지정하기
x=10
y=20
if x==10 and y==20:
    print('참')
else:
    print('거짓')

# 14.4.1 중첩 if 조건문과 논리 연산자
if 0<x<20:
    print('20보다 작은 양수입니다.')

#14.6 연습문제 : 합격 여부 판단하기

written_test=75
coding_test=True
if written_test>=80 and coding_test==1:
    print('합격')
else:
    print('불합격')

# 14.7 심사문제(네 과목의 평균점수가 80점 이상일떄 합격임)
kor=89
eng=72
math=93
sci=82
avg1=(kor+eng+math+sci)/4
x=int(input())
if avg1>=80:
    print('합격')
elif avg1<80:
    print('불합격')
else :
    print('잘못된 점수')
