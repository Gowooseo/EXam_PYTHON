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

# 12.2.2 딕셔너리에 키가 있는지 확인하기
#멤버 연산자를 사용한다.
'health' in lux
print('health' in lux)

'health' not in lux
print('health' not in lux)
# 12.2.3 딕셔너리의 키 개수 구하기
len(lux) #lux 딕셔너리에는 health,mana,melee,armor의 네개의 키가 포함 되어 있으므로....

# 12.4 다음 소스 코드를 완성하여 게임 캐릭터의 체력과 이동속도가 출력되게 만드세요.
camille={
    'health':575.6,
    'health_regen':1.7,
    'mana':338.8,
    'mana_regen':1.63,
    'melee':125,
    'attack_damage':60,
    'attack_speed':0.625,
    'armor':26,
    'magic_resistance':32.1,
    'movement_speed':340

}
print(camille['health'])
print(camille['movement_speed'])
# 하다가 버벅인거 말고는 쉽게 풀었습니다.
# 12.5 심사문제:딕셔너리에 게임 캐릭터 능력치 저장하기

mordekaiser=dict(health=575.6,health_regen=1.7,mana=338.8,mana_regen=1.63)
print(mordekaiser.keys())
print(mordekaiser.values())
# 문제가 말하고자 하는바가 뭔지 잘 모르겠어서 제 나름대로 만들어 보았습니다. 죄송합니다..


# 실제 답안
# [문제]----------------------------------------
# 문자열 여러개와 실수 숫자 여러개를 두 줄로 입력 받기
# - 첫번쨰 입력 받은 값을 Key로
# - 두번재 입력 받은 값을 Value로
# - 최종적으로 딕셔너리로 저장해주세요

#-----------------------------------------------
twoData=input("문자열 4~5개, 실수 숫자 4~5개를 두 줄로 입력\n 단, 문자열과 실수 숫자 갯수는 동일\n(예:ab bb cc dd, 3.1 5.2 6.5 8.1) :")


# key와 value로 데이터 분리
keys,values=twoData.split(',') # 'aa bb cc dd,1.12.23.3.4.4
keys=keys.split # 'aa bb cc dd
values=values.split() # 1.1,2.2,3.3.,4.4
# 입력 데이터 존재 여부 체크(len()이 8또는 10, 또한 값이 실수)
if (len(keys)==4 and len(values)==4) or (len(keys)==5 and len(values)==5) :
    dataDict={}
    if len(keys)==4:
        dataDict[keys[0]]=values[0]
        dataDict[keys[1]]=values[1]
        dataDict[keys[2]]=values[2]
        dataDict[keys[3]]=values[3]

    else:
        dataDict[keys[0]] = values[0]
        dataDict[keys[1]] = values[1]
        dataDict[keys[2]] = values[2]
        dataDict[keys[3]] = values[3]
    print(f'dataDict => {dataDict}')
else:
    print("입력된 데이터가 정확하지 않습니다.")