#----------------
def foo():
    global x # 전역변수 x
    x=20     #wjsdurqustn x에 값 변경
    print(x) # 전역변수 x전역변수 x

# 전역변수-------------------\s=10

#함수 호출----------------------------------
foo(  )
print(x)

print(locals)


def foo():
    global x  # 전역변수 x
    x = 20  # wjsdurqustn x에 값 변경
    print(x)  # 전역변수 x전역변수 x


# 전역변수-------------------\s=10

# 함수 호출----------------------------------
foo()
print(x)

print(locals)