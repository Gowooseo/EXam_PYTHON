#12.1
lux={'health':490,'mana':334,'melee':550,'armor':18.72}
print(lux)
#12.1.1 키 이름 중복
lux={'health':490,'health':800,'mana':334,'melee':550,'armor':18.72}
print(lux)
# 티에는 리스트와 딕셔너리 사용 불가
#12.1.3 빈 딕셔너리 만들기
x={}
y=dict()
# 12.1.4.dict로 딕셔너리 만들기
lux1=dict(health=490,mana=334,melee=550,armor=18.72)
print(lux1)


# 12.2 딕셔너리의 키에 접근하고 값 할당
print(lux['health'])
print(lux['armor'])
# 키를 지정하지 않으면 딕셔너리 전체를 뜻함
# 12.2.1 값 변경
lux['health']=1100
print(lux['health']) # 바뀐것을 확인 가능(딕셔너리[키]=값)
# 없는 키에도 할당 가능
lux['mana regen']=3.28
print(lux)

12.2.2 딕셔너리에 키가 있는지 확인하기


