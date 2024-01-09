# 31.1 재귀호출
# def hello():
#     print('Hello,world! ')
#     hello()
# hello()


#31.1.1 재귀 호출에 종료 조건 만들기

def hello(count):
    if count==0:
        return
    print('Hello,world!',count)

    count-=1
    hello(count)
hello(5)

#31.2 재귀호출로 팩토리얼 구하기
def factorial(n):
    if n==1:
        return 1
    return n *factorial(n-1)
print(factorial(5))
