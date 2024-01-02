#-----------------------------------------------

print(list(range(1,6,2)))

list(range(5,-10,-2))
print(list(range(5,-10,-2)))
msg= tuple(range(-10,9,2))
print(msg)
a=[10,20,0,30]
b=[9,8,7,6]
print(a+b)
#range는 연결 불가, 따라서 이걸 리스트나 튜플로 만들어 연결한다
print(list(range(0,11))+list(range(11,21)))
a='hello'
b='world!'
c=14
print(a+str(c))
# range는 +,* 다 적용 안됨 항상 다른 시퀀스로 바꾸어서 더해줘야 함
fore=list(range(0,5,2))*3
print(fore)
len(range(0,5))
print(len(range(0,5)))

hello='HELLO, WORLD!'
print(len(hello))
hello='안녕하세요'
len(hello.encode('utf-8'))
print()
a=[1,2,3,4,5]
del a[2]
print(a)
a[2]=3
print(a)
a1=list(range(10,91,10))
print(a1)
print(a1[5:1:-1])
print(a1[0:len(a1)])
print(a1[2:len(a1)])
r=range(10)
print(r)
r[4:7]

hello[2:9]
hello='Hello, world!'
hello[2:9]

year=[2011,2012,2013,2014,2015,2016,2017,2018]
population=[10249679,10195318,10143645,10103233,10022181,9930616,9857426,9838892]
print(year[5:8])
print(population[5:8])

n=(-32,75,97,-10,9,32,4,-15,0,76,14,2)
print(n[1::2])

x=list(range(1,11))
del(x[-5:])
print(x)


